import random

print('丁凯峰\n2302190128')
m, n = map(int, input('请输入两个正整数: ').split())
random.seed(m)
ls = []
for i in range(n):
    ls.append(str(random.randint(0, 9)))
print(ls)
set_ls = set(ls)
new_ls = list(set_ls)
new_ls = sorted(new_ls)
print(new_ls)
