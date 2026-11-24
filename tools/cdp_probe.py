"""Run pet-adventures.html in real time in headless Chrome and read results back over DevTools.

Needed for real Web Audio checks: with --virtual-time-budget the audio clock is frozen.
  python3 tools/cdp_probe.py "file:///ABS/PATH/pet-adventures.html#view=audioprobe" 22
  python3 tools/cdp_probe.py "file:///ABS/PATH/pet-adventures.html#view=clicktest&tri" 25
  python3 tools/cdp_probe.py "file:///ABS/PATH/pet-adventures.html#view=jukebox" 4 shot.png   # screenshot
Prints the page's #testout text after WAIT seconds (or saves a PNG if a third argument is given).
"""
import json, os, socket, base64, struct, subprocess, sys, tempfile, time, urllib.request
CH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
url = sys.argv[1]; wait = float(sys.argv[2])
prof = tempfile.mkdtemp(prefix='pet-cdp-')
proc = subprocess.Popen([CH, '--headless=new', '--disable-gpu', '--autoplay-policy=no-user-gesture-required',
                         '--remote-debugging-port=9333', '--window-size=864,480', '--hide-scrollbars', '--user-data-dir=' + prof, url],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    for _ in range(50):
        try:
            tabs = json.load(urllib.request.urlopen('http://127.0.0.1:9333/json')); break
        except Exception: time.sleep(0.2)
    ws = [t for t in tabs if t.get('type') == 'page'][0]['webSocketDebuggerUrl']
    time.sleep(wait)
    host, path = ws[len('ws://'):].split('/', 1)
    h, port = host.split(':')
    s = socket.create_connection((h, int(port)))
    key = base64.b64encode(os.urandom(16)).decode()
    s.sendall(('GET /%s HTTP/1.1\r\nHost: %s\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: %s\r\nSec-WebSocket-Version: 13\r\n\r\n' % (path, host, key)).encode())
    buf = b''
    while b'\r\n\r\n' not in buf: buf += s.recv(4096)
    shot = len(sys.argv) > 3
    msg = json.dumps({'id': 1, 'method': 'Page.captureScreenshot', 'params': {'format': 'png'}} if shot else {'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': "document.getElementById('testout').textContent", 'returnByValue': True}}).encode()
    mask = os.urandom(4)
    hdr = bytes([0x81]) + (bytes([0x80 | len(msg)]) if len(msg) < 126 else bytes([0x80 | 126]) + struct.pack('>H', len(msg)))
    s.sendall(hdr + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(msg)))
    data = b''
    while True:
        data += s.recv(65536)
        if len(data) < 2: continue
        ln = data[1] & 0x7f; off = 2
        if ln == 126: ln = struct.unpack('>H', data[2:4])[0]; off = 4
        elif ln == 127: ln = struct.unpack('>Q', data[2:10])[0]; off = 10
        if len(data) >= off + ln: break
    res = json.loads(data[off:off + ln])['result']
    if shot: open(sys.argv[3], 'wb').write(base64.b64decode(res['data'])); print('saved', sys.argv[3])
    else: print(res['result'].get('value'))
finally:
    proc.terminate()
