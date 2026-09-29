import re
def check_url_v2(url):
    print(f"\n[+] Scanning: {url}")
    score=0; reasons=[]
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score+=3; reasons.append("IP Address")
    if "@" in url:
        score+=2; reasons.append("@ symbol")
    if url.count('.') >= 4:
        score+=2; reasons.append(f"Onk dot ({url.count('.')} ta)")
    if not url.startswith("https://"):
        score+=1; reasons.append("HTTPS nai")
    if any(s in url for s in ["bit.ly","tinyurl","cutt.ly"]):
        score+=2; reasons.append("Short link")
    if url.endswith((".ga",".tk",".ml",".cf",".gq")):
        score+=3; reasons.append("Free suspicious TLD.ga/.tk")
    for b in ["facebook","google","bkash","nagad"]:
        if b in url and f"{b}.com" not in url.split('/')[2]:
            # asol domain check
            if b in url:
                score+=3; reasons.append(f"Fake brand: {b}"); break
    print("-"*30)
    if score>=3:
        print(f"[!] DANGER! Score: {score}/10")
        for r in reasons: print(f" -> {r}")
    else:
        print(f"[OK] Score: {score} -> {reasons}")
    print("-"*30)

print("=== Chottogram Detector v2.1 Fixed ===")
for u in ["https://google.com","http://bit.ly/bkash-offer-5000","http://facebook.com.login.verify-account.ga"]:
    check_url_v2(u)
