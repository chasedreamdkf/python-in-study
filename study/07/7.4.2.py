import pandas as pd
import math


def csv_to_ls(file):
    wine_list = pd.read_csv(file).values.tolist()
    # print(wine_list)
    return wine_list


def country_ls(wine_list):
    """接收列表格式的葡萄酒数据为参数，略过标题行，
    返回不重复的国家名列表，按字母表升序排序，
    若国家名数据缺失，略过该条数据，返回值中不包含空字符串元素。
    """
    ls = []
    for w in wine_list:
        if w[1] not in ls:
            ls.append(w[1])
    ls = sorted(ls)
    return ls


def avg_point(wine_list, country):
    """接收列表格式的葡萄酒数据和国家名列表为参数，
    计算每个国家的葡萄酒的平均得分，
    返回值为国家名和得分的列表。
    """
    ave = []
    for c in country:
        n = 0
        total = 0
        for w in wine_list:
            if c == w[1]:
                n += 1
                total += w[-3]
        ave.append([c, round(total / n, 2)])
    return ave


def avg_point_sort(wine_list, country):
    """接收列表格式的葡萄酒数据和国家名列表为参数，
    计算每个国家的葡萄酒的平均得分，
    返回值为国家名和得分的列表，按评分由高到低降序排列
    """
    ave = []
    for c in country:
        n = 0
        total = 0
        for w in wine_list:
            if c == w[1]:
                n += 1
                total += w[-3]
        ave.append([c, round(total / n, 2)])
    ave = sorted(ave, key=lambda x: x[-1], reverse=True)
    return ave


def top_10_point(wine_list):
    """接收列表格式的葡萄酒数据参数，返回评分最高的十款葡萄酒的编号、出产国、评分和价格，
    按评分降序输出。
    需要注意的是评分可能有缺失值，此时该数据为nan
    if math.isnan(x) == False可用于判定x的值是不是nan
    nan的数据类型是float,不可以直接用字符串判定方法
    """
    wine_list = [[x[0], x[1], x[-3], x[-2]] for x in wine_list if math.isnan(x[-3]) == False]
    wine_list = sorted(wine_list, key=lambda x: x[-2])[-1:-11:-1]
    return wine_list


def top_20_price(wine_list):
    """接收列表格式的葡萄酒数据参数，返回价格最高的二十款葡萄酒的编号、出产国、评分和价格，按价
    格降序输出。
    @参数 wine_list：葡萄酒数据，列表类型
    需要注意的是价格可能有缺失值，此时该数据为nan
    if math.isnan(x) == False可用于判定x的值是不是nan
    nan的数据类型是float,不可以直接用字符串判定方法。
    """
    wine_list = [[x[0], x[1], x[-3], x[-2]] for x in wine_list if math.isnan(x[-2]) == False]
    wine_list = sorted(wine_list, key=lambda x: x[-2])[-1:-21:-1]
    return wine_list


def amount_of_point(wine_list):
    """接收列表格式的葡萄酒数据参数，返回每个评分的葡萄酒数量，忽略没有评分的数据
    例如[...[84, 645], [85, 959],...]表示得分为84的葡萄酒645种，得分85的葡萄酒有959种。
    @参数 wine_list：葡萄酒数据，列表类型
    """
    scores = []
    for w in wine_list:
        if w[-3] not in scores:
            scores.append(w[-3])
    ls = []
    for score in scores:
        n = 0
        for w in wine_list:
            if score == w[-3]:
                n += 1
        ls.append([score, n])
    ls = sorted(ls, key=lambda x: x[0])
    return ls


def most_of_point(amount_of_points):
    """接收每个评分的葡萄酒数量的列表为参数，
    返回获得该分数数量最多的评分和数量的列表。
    """
    amount_of_points = sorted(amount_of_points, key=lambda x: x[-1])
    return amount_of_points[-1]


def avg_price_of_most_point(wine_list, most_of_points):
    """接收列表格式的葡萄酒数据和获得最多的评分及数量的列表为参数
    忽略缺失价格的数据，返回这个分数的葡萄酒的平均价格，保留2位小数。
    """
    prices = [x[-2] for x in wine_list if (x[-3] == most_of_points[0] and math.isnan(x[-2]) == False)]
    ave = round(sum(prices) / len(prices), 2)
    return ave


if __name__ == '__main__':
    print('丁凯峰\n2302190128')
    filename = 'winemag-data.csv'
    wine = csv_to_ls(filename)
    Country = country_ls(wine)
    print('国家名列表:')
    print(Country)
    print('每个国家的葡萄酒的平均得分:')
    print(avg_point(wine, Country))
    print('每个国家的葡萄酒的平均得分降序输出:')
    print(avg_point_sort(wine, Country))
    print('评分最高的十款葡萄酒的编号、出产国、评分和价格，按评分降序输出:')
    print(top_10_point(wine))
    print('价格最高的二十款葡萄酒的编号、出产国、评分和价格，按价格降序输出')
    print(top_20_price(wine))
    amount_point = amount_of_point(wine)
    print('各个评分的葡萄酒数量:')
    print(amount_point)
    Most_point = most_of_point(amount_point)
    print('拥有葡萄酒数量最多的评分和数量:')
    print(Most_point)
    print('拥有葡萄酒数量最多的评分的葡萄酒的平均价格:')
    print(avg_price_of_most_point(wine, Most_point))
