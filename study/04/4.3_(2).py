# 百钱百鸡
print('丁凯峰\n学号: 2302190128')
flag = 0

for cock in range(4, 16, 4):
    for hen in range(4, 20, 1):
        chicken = 100 - cock - hen
        if chicken % 3 == 0 and cock * 5 + hen * 3 + chicken / 3 == 100:
            print('cock: {},hen: {}, chicken: {}'.format(cock, hen, 100 - cock - hen))
            flag = 1
            continue

if flag == 0:
    print('无解')
