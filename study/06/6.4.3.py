def leap(current_date):
    """接收一个用8个字符表示日期的字符串为参数，判断这个日期中的年份是否为闰年,返回值为布尔型。
    @参数 current_date: 表示年份,字符串类型"""
    year = int(current_date)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def legal_judge(current_date):
    """接收一个用8个字符表示日期的字符串为参数，判定日期的合法性，返回值为布尔型。
    @参数 current_date：表示日期，字符串类型"""
    d = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    year = current_date[:4]
    month = int(current_date[4:6])
    day = int(current_date[-2:])
    if month < 1 or month > 12:
        return False
    if leap(year):
        if day <= d[1][month - 1]:
            return True
        else:
            return False
    else:
        if day <= d[0][month - 1]:
            return True
        else:
            return False


def days_of_month(current_date):
    """接收一个用8个字符表示日期的字符串为参数，计算这个日期中的月份有多少天？返回值为整型，
    表示当前月份天数。
    @参数 current_date：表示日期，字符串类型"""
    d = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    year = int(current_date[:4])
    month = int(current_date[4:6])
    if leap(year):
        return d[1][month - 1]
    else:
        return d[0][month - 1]


def name_of_month(current_date):
    """接收一个用8个字符表示日期的字符串为参数，返回这个月份对应的英文单词及其缩写形式。
    @参数 current_date：表示日期，字符串类型"""
    months = [('January', 'Jan.'), ('February', 'Feb.'), ('March', 'Mar.'),
              ('April', 'Apr.'), ('May', 'May.'), ('June', 'Jun.'),
              ('July', 'Jul.'), ('August', 'Aug.'), ('September', 'Sept.'),
              ('October', 'Oct.'), ('November', 'Nov.'), ('December', 'Dec.')]
    month = int(current_date[4:6])
    return months[month - 1]


def separate_date(current_date, symbol):
    """接收一个用8个字符表示日期的字符串和一个符号为参数，返回用该符号分隔的日期，字符串类型。
    @参数 current_date：表示日期，字符串类型
    @参数 symbol：分隔符号，字符串类型"""
    year = current_date[:4]
    month = current_date[4:6]
    day = current_date[-2:]
    return year + symbol + month + symbol + day


if __name__ == '__main__':
    print('丁凯峰\n学号: 2302190128')
    CurrentDate = input()
    sign = input()
    if legal_judge(CurrentDate):
        print(f'{CurrentDate}是合法日期')
        if leap(CurrentDate[:4]):
            print(f'{CurrentDate[:4]}年是闰年')
        else:
            print(f'{CurrentDate[:4]}年不是闰年')
        days = days_of_month(CurrentDate)
        print(f'{CurrentDate[:4]}年{int(CurrentDate[4:6])}月有{days}天')
        print(separate_date(CurrentDate, sign))
        monthName, monthAbbr = name_of_month(CurrentDate)
        print(f'{int(CurrentDate[4:6])}月英文是{monthName}，缩写为{monthAbbr}')
    else:
        print(f'{CurrentDate}是非法日期')
