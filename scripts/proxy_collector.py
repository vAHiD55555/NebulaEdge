import requests, re

def fetch_proxies():
    urls = [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"
    ]
    proxies = set()
    for url in urls:
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            found = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d+\b', r.text)
            proxies.update(found)
        except:
            pass
    return sorted(proxies)

if __name__ == "__main__":
    proxies = fetch_proxies()
    with open("proxies.txt", "w") as f:
        f.write("\n".join(proxies))
    print(f"Collected {len(proxies)} proxies.")