import Cookies from 'universal-cookie';

export function encryptCookieName(cookieName) {
    const md5 = require("crypto-js/md5");
    return md5(cookieName);
}

export function generateAuthHeader() {
    const cookies = new Cookies();
    return {"authorization":"PDB "+ cookies.get(encryptCookieName('authtoken'))}
}

export function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

export function validateNickname(nickname) {
    return nickname.length > 2;
}

export function validatePassword(password) {
    return password.length > 4;
}