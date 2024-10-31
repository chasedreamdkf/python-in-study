print('二鼠打洞')
print('丁凯峰\n学号: 2302190128')

n = int(input('请输入墙的厚度（整数）: '))
rat, mouse, day, time = 1, 1, 0, 1
distance_of_rat, distance_of_mouse = 0, 0
Sum = 0

while Sum < n:
    Sum = 0
    day += 1
    distance_of_rat += rat
    distance_of_mouse += mouse
    Sum += distance_of_mouse + distance_of_rat
    """if Sum >= n:
        break"""
    rat = rat * 2
    mouse = mouse / 2

rat = rat / 2
mouse = mouse * 2
distance_of_rat -= (Sum - n) * (rat / (rat + mouse))
distance_of_mouse -= (Sum - n) * (mouse / (rat + mouse))

print(day)
print(round(distance_of_rat, 1), round(distance_of_mouse, 1))
