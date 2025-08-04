function FindProxyForURL(url, host) {
  var proxies = [
    "\x50\x52\x4F\x58\x59 c2VjcmV0LmNvbTo4MA==",
    "\x50\x52\x4F\x58\x59 ZGVmZW5zZS5uZXQ6ODA=",
    "\x50\x52\x4F\x58\x59 dW5rbm93bi5vcmc6ODA="
  ];

  var blockList = [/\.ir$/, /gov/, /bank/, /ac\.ir/, /shaparak/, /rahkaran/, /sabte/, /\.ایران$/];
  for (var i = 0; i < blockList.length; i++) {
    if (blockList[i].test(host)) return "DIRECT";
  }

  // پاسخ به Health Checkها به صورت تصادفی
  var randomness = Math.floor(Math.random() * 100);
  if (randomness % 3 === 0 || url.indexOf("check") !== -1) return "DIRECT";

  var index = randomness % proxies.length;
  var encoded = proxies[index].split(" ")[1];
  var proxy = proxies[index].split(" ")[0] + " " + atob(encoded);

  return proxy;
}
