import requests

def test_proxy(proxy):
    try:
        r = requests.get("https://httpbin.org/ip", proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=5)
        if r.status_code == 200:
            return True
    except:
        return False
    return False

if __name__ == "__main__":
    working = []
    with open("proxies.txt") as f:
        for proxy in f.read().splitlines():
            if test_proxy(proxy):
                working.append(proxy)
    with open("working_proxies.txt", "w") as f:
        f.write("\n".join(working))
    print(f"Working proxies saved: {len(working)}")