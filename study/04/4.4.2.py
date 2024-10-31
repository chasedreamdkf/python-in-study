# 个人所得税
print('丁凯峰\n学号: 2302190128')
glory = int(input('请输入应发工资薪金金额: '))
guard = int(input('请输入五险一金金额: '))
fee = int(input('请输入个人所得税免征额: '))
Fee = glory - guard - fee
if Fee <= 3000:
    pay = Fee * 0.03
elif Fee <= 12000:
    pay = Fee * 0.1 - 210
elif Fee <= 25000:
    pay = Fee * 0.2 - 1410
elif Fee <= 35000:
    pay = Fee * 0.25 - 2660
elif Fee <= 55000:
    pay = Fee * 0.3 - 4410
elif Fee <= 80000:
    pay = Fee * 0.35 - 7160
else:
    pay = Fee * 0.45 - 15160
print('应缴税款{:.2f}元,实发工资{:.2f}元。'.format(pay, glory - pay))
