with open('alumni.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split()
        print(line)
