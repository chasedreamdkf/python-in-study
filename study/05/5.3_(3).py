def get_error(string):
    try:
        a = float(string)
    except ValueError:
        return False
    else:
        return True


print('丁凯峰\n学号: 2302190128')
s = input('请输入: ')
if get_error(s):
    print('输入的字符串能转换为浮点数')
else:
    print('输入的字符串不能转换为浮点数')
