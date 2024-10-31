# 凯撒密码加密
import string as sr


def caesar_cipher(text):
    intab = sr.ascii_letters + sr.digits
    outtab = sr.ascii_lowercase[3:] + sr.ascii_lowercase[:3] + sr.ascii_uppercase[3:] \
             + sr.ascii_uppercase[:3] + sr.digits[3:] + sr.digits[:3]
    table = str.maketrans(intab, outtab)
    return text.translate(table)


if __name__ == '__main__':
    in_text = input('请输入字符串: ')
    print(caesar_cipher(in_text))
