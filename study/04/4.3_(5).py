print('丁凯峰\n学号: 2302190128')
number = input('请输入座位号: ')
if 'a' in number or 'A' in number or 'f' in number or 'F' in number:
    print('座位在窗口')
elif 'c' in number or 'C' in number or 'd' in number or 'D' in number:
    print('座位在过道')
elif 'b' in number or 'B' in number:
    print('座位在中间')
else:
    print('座位号不存在')
