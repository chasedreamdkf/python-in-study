def say_hi_default(full_name, gender='男'):
    if gender == '男':
        a = '先生'
    elif gender == '女':
        a = '女士'
    else:
        a = '先生/女士'
    return f'尊敬的{full_name}{a},欢迎来到火星!'


print('丁凯峰\n学号:2302190128\n')
person_name = input('请输入姓名: ')
print(say_hi_default(person_name))
print(say_hi_default(person_name, '女'))
