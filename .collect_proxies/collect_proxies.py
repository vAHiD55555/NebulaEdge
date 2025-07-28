import requests
import json
import os

# منابع پراکسی‌ها
PROXY_SOURCES = {
    "http": "https://raw.githubusercontent.com/vAHiD55555/Free-Proxies/main/proxy_files/http_proxies.txt",
    "https": "https://raw.githubusercontent.com/vAHiD55555/Free-Proxies/main/proxy_files/https_proxies.txt",
    "socks4": "https://raw.githubusercontent.com/vAHiD55555/Free-Proxies/main/proxy_files/socks4_proxies.txt",
    "socks5": "https://raw.githubusercontent.com/vAHiD55555/Free-Proxies/main/proxy_files/socks5_proxies.txt",
    "json": "https://raw.githubusercontent.com/vAHiD55555/Free-Proxies/main/proxy_files/proxies_dump.json"
}

def fetch_proxies():
    proxies = []
    for proto, url in PROXY_SOURCES.items():
        try:
            res = requests.get(url, timeout=15)
            if res.ok:
                if proto == "json":
                    data = res.json()
                    proxies.extend(data.get("proxies", []))
                else:
                    lines = res.text.strip().splitlines()
                    for line in lines:
                        ip, port = line.strip().split(":")
                        proxies.append({
                            "ip": ip,
                            "port": port,
                            "type": proto.upper()
                        })
        except Exception as e:
            print(f"[{proto}] Failed to fetch: {e}")
    return proxies

def save_output(proxies, path="outputs/proxies.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(proxies, f, indent=2)
    print(f"[+] Saved {len(proxies)} proxies to {path}")

if __name__ == "__main__":
    proxy_list = fetch_proxies()
    save_output(proxy_list)
