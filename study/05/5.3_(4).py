def p(a, b , c):
    print(f'这是一辆{a}年生产，型号是{b}的{c}汽车')


print('丁凯峰\n学号: 2302190128')
year, model, brand = input('请输入汽车的生产日期、型号、品牌 : ').split()
p(year, model, brand)
