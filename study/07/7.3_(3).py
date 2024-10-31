print('丁凯峰 2302191028')
try:
    n = int(input('请输入学生人数'))
except ValueError:
    print('ERROR')
ls = []
for i in range(n):
    num, name, phone = input('请输入学号，姓名，电话号码: ').split()
    l = [num.replace(num[4:11], '*' * 7), name.replace(name[1], '*'), phone.replace(phone[3:7], '*' * 4)]
    ls.append(l)
print(ls)
