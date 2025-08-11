def generate_pac(proxies):
    pac = 'function FindProxyForURL(url, host) {\n'
    if proxies:
        pac += '    return "PROXY ' + proxies[0] + '";\n'
    else:
        pac += '    return "DIRECT";\n'
    pac += '}\n'
    return pac

if __name__ == "__main__":
    with open("working_proxies.txt") as f:
        proxies = f.read().splitlines()
    with open("proxy.pac", "w") as f:
        f.write(generate_pac(proxies))
    print("PAC file generated.")