print('丁凯峰\n学号: 2302160128')
had_account = [['aaa', '123456'], ['bbb', '888888'], ['ccc', '333333']]
accounts = [x[0] for x in had_account]
user_account = input('请输入您的账号: ')
user_password = input('请输入密码: ')
if user_account in accounts:
    for account in had_account:
        if user_account == account[0]:
            if user_password == account[1]:
                print('Success')
                break
            else:
                print('Fail')
                break
else:
    print('Wrong User')
