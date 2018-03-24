import Cookies from 'universal-cookie';

export function encryptCookieName(cookieName) {
    const md5 = require("crypto-js/md5");
    return md5(cookieName);
}

export function generateAuthHeader() {
    const cookies = new Cookies();
    return {"authorization":"PDB "+ cookies.get(encryptCookieName('authtoken'))}
}