import requests
import json
import os

OUTPUT_FILE = "outputs/proxies.json"
SOURCES = [
    "https://raw.githubusercontent.com/vAHiD55555/getproxy/refs/heads/master/file/all.txt",
    "https://raw.githubusercontent.com/vAHiD55555/getproxy/refs/heads/master/file/https.txt",
    "https://raw.githubusercontent.com/vAHiD55555/getproxy/refs/heads/master/file/socks5.txt"
]

def clean(proxies):
    seen = set()
    result = []
    for p in proxies:
        p = p.strip()
        if not p or p.startswith('#'): continue
        if ':' in p and p not in seen:
            seen.add(p)
            result.append(p)
    return result

def main():
    all_lines = []
    for url in SOURCES:
        try:
            print(f"Downloading {url}")
            r = requests.get(url, timeout=10); r.raise_for_status()
            all_lines.extend(r.text.splitlines())
        except Exception as e:
            print(f"Failed {url}: {e}")
    proxies = clean(all_lines)
    os.makedirs("outputs", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(proxies, f, indent=2)
    print(f"Saved {len(proxies)} proxies to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
