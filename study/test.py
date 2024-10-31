# write your code here
# read data from console
n = int(input())
# output the answer to the console according to the requirements of the question
lst = [1, 0]
for i in range(1, n + 1):
    cur = [1]
    # print(cur, lst)
    j = 0
    while len(cur) < i:
        cur.append(lst[j] + lst[j + 1])
        j += 1
    print(*cur)
    cur.append(0)
    lst = cur
