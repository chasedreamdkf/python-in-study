# 
n = int(input())
m = 0
while n > 1:
    print(n, end=' ')
    if n % 2 == 0:
        n = n / 2
        m += 1
    else:
        n = n * 3 + 1
        m += 1
print(n, m, sep='\n')
