def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()


def classify_char(txt):
    upper = 0
    lower = 0
    digit = 0
    space = 0
    other = 0
    for char in txt:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        else:
            other += 1
    return upper, lower, digit, space, other


if __name__ == '__main__':
    text = read_file('2.txt')
    classify = classify_char(text)
    print('大写字母: {}\n小写字母: {}\n数字字符: {}\n空白字符: {}\n其他字符: {}'.format(*classify))
