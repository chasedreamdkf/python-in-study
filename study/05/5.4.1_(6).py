def say_hi_multi_parameter(*names):
    for name in names:
        print(f'{name},你好!')


print('丁凯峰\n学号: 2302190128\n')
say_hi_multi_parameter('孟浩然')
say_hi_multi_parameter('杜甫', '李白', '柳宗元', '李商隐')
