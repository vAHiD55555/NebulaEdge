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
    cleaned = []
    for proxy in proxies:
        if proxy not in seen and ":" in proxy:
            seen.add(proxy)
            cleaned.append(proxy.strip())
    return cleaned

def main():
    proxies = []
    for url in SOURCES:
        try:
            print(f"🔗 Downloading from {url}")
            r = requests.get(url, timeout=10)
            lines = r.text.strip().splitlines()
            proxies.extend(lines)
        except Exception as e:
            print(f"⚠️ Failed to download from {url}: {e}")

    proxies = clean(proxies)

    os.makedirs("outputs", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(proxies, f, indent=2)

    print(f"✅ Downloaded and saved {len(proxies)} proxies to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
