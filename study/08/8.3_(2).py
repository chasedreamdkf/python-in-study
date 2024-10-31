print('丁凯峰\n2302190128')
num = set(x for x in '0123456789')
# print(num)
for age in range(11, 100, 1):
    age3 = age ** 3
    age4 = age ** 4
    s_age = str(age3) + str(age4)
    set_age = set(x for x in (str(age ** 4) + str(age ** 3)))
    if len(str(age3)) == 4 and len(str(age4)) == 6 and set_age == num:
        # print(set_age)
        print(f'维纳当年的年龄为: {age}')
        break
