import json
from obfuscation_utils import obfuscate_url, create_fake_cdn
from pathlib import Path

INPUT_PATH = Path("../inputs/proxies_dump.json")
OUTPUT_PATH = Path("../docs")

def load_proxies():
    with open(INPUT_PATH, "r") as f:
        return json.load(f)

def generate_pac(proxies):
    lines = ["function FindProxyForURL(url, host) {"]
    lines.append("  if (shExpMatch(host, '*.trusted.com')) return 'DIRECT';")
    for proxy in proxies:
        obf = obfuscate_url(proxy["server"])
        lines.append(f"  if (dnsDomainIs(host, '{create_fake_cdn()}')) return 'HTTPS {obf}';")
    lines.append("  return 'DIRECT'; }")
    return "\n".join(lines)

def save_file(content, path):
    with open(path, "w") as f:
        f.write(content)

def main():
    proxies = load_proxies()
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    save_file(generate_pac(proxies), OUTPUT_PATH / "pac/proxy_stealth_warrior.pac")
    # مشابه همین می‌تونی برای Clash و Singbox هم اضافه کنی

if __name__ == "__main__":
    main()
