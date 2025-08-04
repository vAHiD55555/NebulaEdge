function FindProxyForURL(url, host) {
  var encoded = "Y2RuLmV4YW1wbGUuY29tOjgw"; // Base64 مسیر پراکسی
  var proxy = "PROXY " + atob(encoded);

  var blacklist = ["ir", "gov", "bank", "ac.ir"];
  for (var i = 0; i < blacklist.length; i++) {
    if (host.indexOf(blacklist[i]) !== -1) {
      return "DIRECT";
    }
  }

  // Health Check به صورت تصادفی برای جلوگیری از شناسایی الگو
  if (Math.random() > 0.5) {
    return proxy;
  } else {
    return "DIRECT";
  }
}
