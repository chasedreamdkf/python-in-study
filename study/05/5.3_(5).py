def c_to_f(c):
    return c * 1.8 + 32


def f_to_c(f):
    return (f - 32) / 1.8


print('丁凯峰\n学号: 2302190128')
tem = input('请输入华氏温度或摄氏温度: ')
if 'c' in tem or 'C' in tem:
    tem1 = float(tem[0: (len(tem) - 1)])
    print('{}摄氏度 = {:.2f}华氏度'.format(tem[0: (len(tem) - 1)], c_to_f(tem1)))
elif 'f' in tem or 'F' in tem:
    tem1 = float(tem[0: (len(tem) - 1)])
    print('{}华氏度 = {:.2f}摄氏度'.format(tem[0: (len(tem) - 1)], f_to_c(tem1)))
else:
    print('输入错误')
