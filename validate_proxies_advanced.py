import json
import requests
from concurrent.futures import ThreadPoolExecutor
import time

INPUT_FILE = "outputs/proxies.json"
OUTPUT_FILE = "outputs/validated_detailed_proxies.json"
TIMEOUT = 7

def get_country(proxy):
    try:
        response = requests.get(f"http://ip-api.com/json/{proxy.split(':')[0]}", timeout=TIMEOUT)
        data = response.json()
        return data.get("country", "Unknown")
    except:
        return "Unknown"

def test_proxy(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    try:
        start = time.time()
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=TIMEOUT)
        latency = time.time() - start
        if response.ok:
            return {
                "proxy": proxy,
                "latency": round(latency, 2),
                "country": get_country(proxy)
            }
    except:
        return None

def main():
    with open(INPUT_FILE, "r") as f:
        proxies = json.load(f)

    print(f"📡 شروع تست روی {len(proxies)} پروکسی")

    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(test_proxy, proxies))

    valid_proxies = [res for res in results if res]

    with open(OUTPUT_FILE, "w") as f:
        json.dump(valid_proxies, f, indent=4)

    print(f"✅ تعداد پروکسی‌های سالم: {len(valid_proxies)}")
    for p in valid_proxies[:5]:  # نمایش چند نمونه
        print(f"• {p['proxy']} — {p['country']} — {p['latency']}s")

if __name__ == "__main__":
    main()
