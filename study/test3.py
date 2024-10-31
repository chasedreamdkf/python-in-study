data = []

with open("MyPython.txt", 'r', encoding='utf-8') as lines:
    for line in lines:
        data.append(line.split())

# print(*data, sep='\n')

with open("MyPython1.txt", 'w+', encoding='utf-8') as file:
    for d in data:
        file.write(d[0])
        file.write(' ')
