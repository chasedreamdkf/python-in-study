# ------------      -------    --------    -----------    -----------
# @File       : 6.4.3 日期分析处理实验模板.py    
# @Contact    : vasp@qq.com
# @Copyright  : 2018-2025, Wuhan University of Technology
# @Modify Time: 2021/4/27 15:27
# @Author     : 赵广辉
# @Version    : 1.0
# @License    : 仅限用于Python程序设计基础实践教程(赵广辉,高等教育出版社)配套实验
# ------------      -------    --------    -----------    -----------


def leap(current_date):
    """接收一个用8个字符表示日期的字符串为参数，判断这个日期中的年份是否为闰年
    返回值为布尔型。
    @参数 current_date：表示日期，字符串类型
    闰年的判定方法是：能被400整除或能被4整除且同时不能被100整除的是闰年。
    # >>> test_date = '20000426'
    # >>> leap(test_date)
    # True
    # >>> test_date = '19000426'
    # >>> leap(test_date)
    # False
    # >>> test_date = '19990426'
    # >>> leap(test_date)
    # False
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def legal_judge(current_date):
    """接收一个用8个字符表示日期的字符串为参数，判定日期的合法性，返回值为布尔型。
    1，3，5，7，8，10，12月各31天，4，6，9，11各30天，闰年2月29天，平年2月28天。
    @参数 current_date：表示日期，字符串类型
    # >>> test_date = '20000426'
    # >>> legal_judge(test_date)
    # True
    # >>> test_date = '19000229'
    # >>> legal_judge(test_date)
    # False
    # >>> test_date = '19990431'
    # >>> legal_judge(test_date)
    # False
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def days_of_month(current_date):
    """接收一个用8个字符表示日期的字符串为参数，计算这个日期中的月份有多少天？返回值为整型，
    表示当前月份天数。
    @参数 current_date：表示日期，字符串类型
    # >>> test_date = '20000826'
    # >>> days_of_month(test_date)
    # 31
    # >>> test_date = '19000226'
    # >>> days_of_month(test_date)
    # 28
    # >>> test_date = '19800226'
    # >>> days_of_month(test_date)
    # 29
    # >>> test_date = '19990430'
    # >>> days_of_month(test_date)
    # 30
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def name_of_month(current_date):
    """接收一个用8个字符表示日期的字符串为参数，返回这个月份对应的英文单词及其缩写形式。
    @参数 current_date：表示日期，字符串类型
    例如：current_date为20201031，返回值为'October','Oct.'
    # >>> test_date = '20000826'
    # >>> name_of_month(test_date)
    # ('August', 'Aug.')
    # >>> test_date = '19000226'
    # >>> name_of_month(test_date)
    # ('February', 'Feb.')
    # >>> test_date = '19801226'
    # >>> name_of_month(test_date)
    # ('December', 'Dec.')
    # >>> test_date = '19990430'
    # >>> name_of_month(test_date)
    # ('April', 'Apr.')
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def separate_date(current_date, symbol):
    """接收一个用8个字符表示日期的字符串和一个符号为参数，返回用该符号分隔的日期，字符串类型。
    @参数 current_date：表示日期，字符串类型
    @参数 symbol：分隔符号，字符串类型
    例如传入'20201031'和"/",返回字符串'2020/09/09'
    # >>> test_date = '20000826'
    # >>> sep = '/'
    # >>> separate_date(test_date, sep)
    # '2000/08/26'
    # >>> test_date = '19801226'
    # >>> sep = '-'
    # >>> separate_date(test_date, sep)
    # '1980-12-26'
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


if __name__ == '__main__':
    CurrentDate = input()
    sign = input()
    if leap(CurrentDate[:4]):
        print(f'{CurrentDate[:4]}年是闰年')
    else:
        print(f'{CurrentDate[:4]}年不是闰年')
    days = days_of_month(CurrentDate)
    print(f'{CurrentDate[:4]}年{int(CurrentDate[4:6])}月有{days}天')
    print(separate_date(CurrentDate, sign))
    if legal_judge(CurrentDate):
        print(f'{CurrentDate}是合法日期')
    else:
        print(f'{CurrentDate}是非法日期')
    monthName, monthAbbr = name_of_month(CurrentDate)
    print(f'{int(CurrentDate[4:6])}月英文是{monthName}，缩写为{monthAbbr}')
