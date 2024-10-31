print('丁凯峰\n学号: 2302190128')
ID = input('请输入身份证号: ')
year = ID[6:10]
month = ID[10:12]
day = ID[12:14]
if int(ID[-2]) % 2 == 0:
    male = '女'
else:
    male = '男'
print("出生: {}年{}月{}日\n性别: {}".format(year, month, day, male))
