def to_int(l):
    for i in range(len(l)):
        l[i] = int(l[i])


print('丁凯峰 2302191028')
l1 = input()
l2 = input()
l1 = l1.split()
l2 = l2.split()
l1.extend(l2)
l3 = sorted(l1, key=lambda x: int(x), reverse=True)
to_int(l3)
print(l3)
