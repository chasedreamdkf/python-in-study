def to_kg(x):
    if x[-1] == 't':
        return float(x[:-1]) * 1000
    else:
        return float(x[:-2])


print('丁凯峰 2302191028\n请输入动物名及其体重:')
animal_informations = []
while 1:
    try:
        animal_information = input()
        animal_information = animal_information.split()
        animal_informations.append(animal_information)
    except:
        print('输入结束')
        break


print(sorted(animal_informations, key=lambda x: to_kg(x[1])))
