def morse_code(text):
    ls = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
          ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")
    print(len(ls))
    out = []
    for i in text:
        if 97 <= ord(i) <= 122:
            out.append(ls[ord(i) - 97])
        elif 0 <= ord(i) <= 25:
            out.append(ls[ord(i)])
        elif 1 <= int(i) <= 10:
            out.append(ls[int(i)])
    return out


if __name__ == '__main__':
    t = input()
    print(morse_code(t))
