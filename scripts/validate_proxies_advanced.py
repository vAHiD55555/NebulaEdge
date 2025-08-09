import json
import requests
from concurrent.futures import ThreadPoolExecutor
import time

INPUT_FILE = "outputs/proxies.json"
OUTPUT_FILE = "outputs/validated_detailed_proxies.json"
TIMEOUT = 7

def get_country(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip.split(':')[-2].split('/')[-1]}", timeout=TIMEOUT)
        return r.json().get("country", "Unknown")
    except:
        return "Unknown"

def test_proxy(proxy):
    proto, addr = proxy.split("://") if "://" in proxy else ("http", proxy)
    proxies = {proto: proxy}
    try:
        start = time.time()
        r = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=TIMEOUT)
        latency = round(time.time() - start, 2)
        if r.ok:
            return {"proxy": proxy, "latency": latency, "country": get_country(proxy)}
    except:
        pass
    return None

def main():
    with open(INPUT_FILE) as f:
        proxies = json.load(f)
    print(f"Testing {len(proxies)} proxies...")
    with ThreadPoolExecutor(max_workers=20) as ex:
        results = list(ex.map(test_proxy, proxies))
    valid = [r for r in results if r]
    os.makedirs("outputs", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(valid, f, indent=2)
    print(f"Found {len(valid)} valid proxies")

if __name__ == "__main__":
    main()
