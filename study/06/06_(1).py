def s_um(id, w):
    s = [int(x) * y for x in id for y in w]
    return sum(s)


print('丁凯峰\n学号: 230290128')
intab = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
outtab = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
# print(outtab)
initial_id = input('请输入原身份证号: ')
W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
new_id = initial_id[0:6] + '20' + initial_id[6:]
S = s_um(new_id, W)
n = 0
for i in range(0, 17, 1):
    if str(S % 11) == intab[i]:
        n = i
        break
new_id = new_id + outtab[n]
print(new_id)
