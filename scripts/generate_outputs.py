import json
import os
import gzip

INPUT_FILE = "outputs/validated_detailed_proxies.json"
OUTPUT_DIR = "outputs"
TXT    = os.path.join(OUTPUT_DIR, "proxies.txt")
JSON   = os.path.join(OUTPUT_DIR, "proxies_clean.json")
PAC    = os.path.join(OUTPUT_DIR, "proxy.pac")
PAC_MIN= os.path.join(OUTPUT_DIR, "proxy.min.pac")
PAC_GZ = os.path.join(OUTPUT_DIR, "proxy.pac.gz")

def load_proxies():
    data = json.load(open(INPUT_FILE))
    return [item["proxy"] for item in data]

def write_txt(ps):
    open(TXT,"w").write("\\n".join(ps))

def write_json(ps):
    json.dump(ps, open(JSON,"w"), indent=2)

def write_pac(ps):
    head = "function FindProxyForURL(url, host){"
    body = f"return 'PROXY {ps[0]}; DIRECT';"
    tail = "}"
    open(PAC,"w").write(head+body+tail)

def minify_pac():
    data = open(PAC).read()
    open(PAC_MIN,"w").write(data.replace(" ","").replace("\\n",""))

def gzip_pac():
    with open(PAC,"rb") as f, gzip.open(PAC_GZ,"wb") as gz:
        gz.writelines(f)

if __name__=="__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ps = load_proxies()
    write_txt(ps)
    write_json(ps)
    write_pac(ps)
    minify_pac()
    gzip_pac()
    print("Generated all outputs.")
