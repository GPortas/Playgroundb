export function encryptCookieName(cookieName) {
    var md5 = require("crypto-js/md5");
    return md5(cookieName);
}