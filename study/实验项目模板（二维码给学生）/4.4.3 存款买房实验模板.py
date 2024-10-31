# ------------      -------    --------    -----------    -----------
# @File       : 4.4.3 存款买房实验模板.py    
# @Contact    : vasp@qq.com
# @Copyright  : 2018-2025, Wuhan University of Technology
# @Modify Time: 2021/4/26 22:35
# @Author     : 赵广辉
# @Version    : 1.0
# @License    : 仅限用于Python程序设计基础实践教程(赵广辉,高等教育出版社)配套实验
# ------------      -------    --------    -----------    -----------
import math


def type_judge(question):
    """接收一个字符串为参数，根据参数调用不同函数执行不同代码。
    这种写法不规范，但把输入、输出都放在一个函数中，方便管理。
    """
    if question == 'A':
        buy_house()  # 调用解决问题A的程序
    elif question == 'B':
        buy_house_pay_increases()  # 调用解决问题B的程序
    elif question == 'C':
        buy_house_interest()  # 调用解决问题C的程序
    else:
        print('输入错误')


def buy_house():
    """
    1.将你想购买的房子的总价称为total_cost。
    2.将要求支付的首付部分所需的费用部分称为portion_down_payment。假设portion_down_payment = 0.30（30%）。
    3.将存款金额称为current_savings。你的存款从0 元开始。
    4.假设你的年薪是annual_salary，按12 个月平均发放，单位是元。
    5.假设你每个月都要拿出一定数额的工资来存首付。称为portion_saved。此值为一个表示百分比的整数，例如50 表示50%。
    写一个程序来计算你需要多少个月才能攒够钱付定金，不足一个月按一个月计算。
    你的程序要给出以下提示并要求用户输入相应的数值以增加程序的用户友好性：
    1. 请输入总房价：total_cost
    2. 请输入年薪：annual_salary
    3. 请输入月存款比例：portion_saved
    测试用例
    请输入总房价：1000000
    请输入年薪：156800
    请输入月存款比例：60
    输出：需要39 个月可以存够首付
    """
    total_cost = float(input('请输入总房价：'))   # total_cost为当前房价
    annual_salary = float(input('请输入年薪：'))  # 年薪
    portion_saved = float(input('请输入月存款比例：')) / 100  # 月存款比例，输入30转为30%

    # 根据首付款比例计算首付款金额和每个月需要存款数额
    # =======================================================
    # 补充你的代码
    # =======================================================
    print('首付', down_payment)
    print('月存款', monthly_deposit)

    # 计算多少个月才能存够首付款，结果为整数，不足1月按1个月计算，即向上取整
    # =======================================================
    # 补充你的代码
    # =======================================================
    print(f'需要{math.ceil(number_of_months)}个月可以存够首付')

    down_payment = portion_down_payment * total_cost  # 首付款
    current_savings = 0  # 存款金额，从0开始
    monthly_deposit = annual_salary / 12 * portion_saved  # 月存款
    print('首付', down_payment)
    print('月存款', round(monthly_deposit, 2))
    # 计算多少个月才能存够首付款，结果为整数，不足1月按1个月计算，即向上取整
    number_of_months = 0
    while current_savings < down_payment:
        number_of_months = number_of_months + 1
        current_savings = current_savings + monthly_deposit
        print(number_of_months, '当前存款', round(current_savings, 2))

    print(number_of_months)
    print(f'需要{math.ceil(number_of_months)}个月可以存够首付')
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def buy_house_pay_increases():
    """
    1.让用户输入半年度加薪的整数百分比，例如输入7表示每半年加薪7%。
    2.第6个月后，按该百分比增加薪资。在第12个月、18个月之后，依此类推（只有在第6、12、18……等月份时才加薪）。
    写一个程序计算需要多少个月才能攒够钱付首付款。与之前一样，假设所需的首付款百分比为0.30（30%）。
    你的程序要给出以下提示并要求用户输入相应的数值：
    1. 请输入总房价：total_cost
    2. 请输入年薪：annual_salary
    3. 请输入月存款比例：portion_saved
    4. 每半年加薪比例：semi_annual_raise
    测试用例
    请输入总房价：1000000
    请输入年薪：156800
    请输入月存款比例：60
    请输入加薪比例：7
    输出：需要33 个月可以存够首付
    """
    total_cost = float(input('请输入总房价：'))  # total_cost为当前房价
    annual_salary = float(input('请输入年薪：'))  # 年薪
    portion_saved = float(input('请输入月存款比例：')) / 100  # 月存款比例，输入30转为30%
    semi_annual_raise = float(input('请输入加薪比例：'))  # 输入每半年加薪比例

    portion_down_payment = 0.3  # 首付比例，浮点数
    down_payment = portion_down_payment * total_cost  # 首付款
    current_savings = 0  # 存款金额，从0开始
    monthly_salary = annual_salary / 12  # 月薪
    monthly_deposit = monthly_salary * portion_saved
    # 计算多少个月才能存够首付款，结果为整数，不足1月按1个月计算，即向上取整
    number_of_months = 0
    while current_savings < down_payment:
        number_of_months = number_of_months + 1
        if number_of_months % 6 == 0:  # 月份为6的整数倍时，加薪
            monthly_salary = monthly_salary * (1 + semi_annual_raise / 100)  # 加薪后的月薪
            monthly_deposit = monthly_salary * portion_saved  # 加薪后的月存款
        current_savings = current_savings + monthly_deposit  # 当前累计存款
        # print(number_of_months, round(monthly_deposit, 2))   # 输出每个月存款情况

    print(f'需要{math.ceil(number_of_months)}个月可以存够首付')

    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def buy_house_interest():
    """
    假设你每个月都是月初发工资，同时会收到上一个月的存款利息。假设所需的首付款百分比为0.30（30%），
    存款年利率interest_rate 为2.25%，每半6 个月加一次薪水，修改你的程序，计算存够首付需要多少个月。
    你的程序要给出以下提示并要求用户输入相应的数值：
    1. 请输入总房价：total_cost
    2. 请输入年薪：annual_salary
    3. 请输入月存款比例：portion_saved
    4. 每半年加薪比例：semi_annual_raise
    5. 请输入存款年利率：
    测试用例：
    请输入总房价：1000000
    请输入年薪：156800
    请输入月存款比例：60
    请输入加薪比例：7
    输出：需要32 个月可以存够首付
    """
    total_cost = float(input('请输入总房价：'))  # total_cost为当前房价
    annual_salary = float(input('请输入年薪：'))  # 年薪
    portion_saved = float(input('请输入月存款比例：')) / 100  # 月存款比例，输入30转为30%
    semi_annual_raise = float(input('请输入加薪比例：'))  # 输入每半年加薪比例

    portion_down_payment = 0.3  # 首付比例，浮点数
    down_payment = portion_down_payment * total_cost  # 首付款
    current_savings = 0  # 存款金额，从0开始
    monthly_salary = annual_salary / 12  # 月薪
    monthly_deposit = monthly_salary * portion_saved
    # 计算多少个月才能存够首付款，结果为整数，不足1月按1个月计算，即向上取整
    number_of_months = 0
    while current_savings < down_payment:
        number_of_months = number_of_months + 1
        if number_of_months % 6 == 0:  # 月份为6的整数倍时，加薪
            monthly_salary = monthly_salary * (1 + semi_annual_raise / 100)  # 加薪后的月薪
            monthly_deposit = monthly_salary * portion_saved  # 加薪后的月存款
            print(number_of_months, round(monthly_deposit, 2))
        current_savings = current_savings * (1 + 0.025 / 12) + monthly_deposit  # 当前累计存款
    print(f'需要{math.ceil(number_of_months)}个月可以存够首付')

    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


if __name__ == '__main__':
    choice = input()    # 接收用户输入的字符串
    type_judge(choice)  # 调用判断输入的函数决定执行哪个函数
