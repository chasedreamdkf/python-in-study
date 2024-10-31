# 凯撒密码解密
import string

low = string.ascii_lowercase
up = string.ascii_uppercase
dig = string.digits
intab = low + up + dig


def caesar_decrypt(text, offset):
    """解密"""
    outtab = low[offset:] + low[:offset] + up[offset:] + up[:offset] + dig[offset:] + dig[:offset]
    table = str.maketrans(outtab, intab)
    return text.translate(table)


def find_offset(kay_text, ciphertext):
    """寻找偏移量"""
    for i in range(26, 0, -1):
        outtab = low[i:] + low[:i] + up[i:] + up[:i] + dig[i:] + dig[:i]
        table = str.maketrans(outtab, intab)
        if kay_text in ciphertext.translate(table):
            return i


if __name__ == '__main__':
    key_message = 'question'
    cipher_text = 'Yt gj,tw sty yt gj,ymfy nx f vzjxynts.'
    taget_text = 'Fyyfhp ts Ujfwq Mfwgtw ts Ijhjrgjw 2, 6496'
    secret_kay = find_offset(key_message, cipher_text)
    print(f'密钥是: {secret_kay}')
    print(caesar_decrypt(taget_text, secret_kay))
