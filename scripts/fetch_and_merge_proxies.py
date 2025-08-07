import os
import re
import json
import requests
from proxy_sources import PROXY_SOURCES

OUTPUT_DIR = "outputs"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "proxies.json")

def normalize_line(line, default_protocol="http"):
    line = line.strip()
    if not line or line.startswith("#"):
        return None

    # Already in full format
    if "://" in line:
        return line.lower()

    # Try to guess protocol
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}:\d+$", line):
        return f"{default_protocol}://{line}"

    return None

def fetch_url(url, default_protocol):
    print(f"Fetching: {url}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            lines = response.text.splitlines()
            return [normalize_line(line, default_protocol) for line in lines]
        else:
            print(f"Failed to fetch {url}: HTTP {response.status_code}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return []

def load_local_file(path, default_protocol):
    print(f"Loading local file: {path}")
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return []

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        return [normalize_line(line, default_protocol) for line in lines]

def collect_all_proxies():
    all_proxies = set()

    for entry in PROXY_SOURCES:
        source_type = entry.get("type")
        location = entry.get("location")
        protocol = entry.get("protocol", "http")

        proxies = []

        if source_type == "url":
            proxies = fetch_url(location, protocol)
        elif source_type == "file":
            proxies = load_local_file(location, protocol)
        else:
            print(f"Unknown source type: {source_type}")
            continue

        clean_proxies = [p for p in proxies if p]
        all_proxies.update(clean_proxies)

    return sorted(all_proxies)

def save_to_file(proxies):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(proxies, f, indent=2)
    print(f"Saved {len(proxies)} proxies to {OUTPUT_FILE}")

if __name__ == "__main__":
    all_proxies = collect_all_proxies()
    save_to_file(all_proxies)
