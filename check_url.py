import re

def check_url(url):
    print(f"\n[+] Checking: {url}")
    sus = []
    if url.count('.') > 3: sus.append("Too many dots")
    if "faceboook" in url or "bkash-offer" in url: sus.append("Fake brand name")
    if "@" in url: sus.append("Has @ symbol")
    if not url.startswith("https://"): sus.append("No HTTPS")
    if sus:
        print("[!] DANGER - Phishing!")
        for s in sus: print(f" - {s}")
    else:
        print("[OK] Safe")
    print("-"*30)

print("=== Chottogram Detector v1 ===")
while True:
    u = input("\nURL (q to quit): ")
    if u=='q': break
    if u: check_url(u)
