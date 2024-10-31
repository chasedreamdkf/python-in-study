def say_hi_gender(full_name, gender):
    if gender == '男':
        a = '先生'
    elif gender == '女':
        a = '女士'
    else:
        a = '先生/女士'
    return f'尊敬的{full_name}{a},欢迎来到火星!'


print('丁凯峰\n学号: 2302190128\n')
person_name = input('请输入姓名: ')
person_gender = input('请输入性别: ')
print(say_hi_gender(person_name, person_gender))
