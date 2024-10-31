"""@作者: 朱正勇, 用于实现爬取数据的可视化"""

import matplotlib.pyplot as plt
import pandas as pd


def show():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
    # 数据读取
    data = pd.read_excel('D:/Code/Py_projects/PythonWork/腾讯课堂课程数据.xlsx').values.tolist()
    x0 = len(data)
    # print(*data, sep='\n')
    # 数据分类
    # 计算机类
    com = [x for x in data if
           "python" in x[0] or "Python" in x[0] or "Java" in x[0] or "C语言" in x[0] or "人工智能" in x[0] or "linux" in
           x[0] or "生物信息" in x[0] or "华算" in x[0]]
    x1 = len(com)
    # 医学类
    med = [x for x in data if
           "护师" in x[0] or "护上" in x[0] or "护理" in x[0] or "兽医" in x[0] or "针灸" in x[0] or "护资" in x[
               0] or "中医" in x[0]]
    x2 = len(med)
    # 大物类
    phy = [x for x in data if
           "电气" in x[0] or "物理" in x[0] or "机器" in [0] or "动力" in x[0] or "光伏" in x[0] or "电子" in x[0]]
    x3 = len(phy)
    # 图画制作类
    dra = [x for x in data if "绘图" in x[0] or "会制" in x[0] or "插画" in x[0]]
    x4 = len(dra)
    # 财政类
    fan = [x for x in data if "财务" in x[0] or "政治" in x[0] or "会计" in x[0] or "经济" in x[0]]
    x5 = len(fan)
    # 传统学科类
    sub = [x for x in data if "英语" in x[0] or "数学" in x[0] or "诗文" in x[0] or "高中生物" in x[0]]
    x6 = len(sub)
    # 工程建设类
    pro = [x for x in data if
           "建筑" in x[0] or "建造" in x[0] or "施工" in x[0] or "消防" in x[0] or "实操" in x[0] or "建造" in x[
               0] or "工程师" in x[0] or "安装" in x[0] or "汽车" in x[0] or "汽修" in x[0]]
    x7 = len(pro)
    # 软件运用类
    sot = [x for x in data if "软件" in x[0] or "CCS" in x[0] or "机器" in x[0] or "设计" in x[0]]
    x8 = len(sot)
    #  其他
    other = [x for x in data if x not in com and x not in med and x not in phy and x not in dra
             and x not in fan and x not in sub and x not in pro and x not in sot]
    x9 = len(other)

    labels = ['计算机类', '医学类', '大物类', '图画制作类', '财政类', '传统学科类', '工程建设类', '软件运用类', '其他']
    sizes = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
    dicts = zip(labels, sizes)
    dicts = sorted(dicts, key=lambda x: x[1])
    # print(*dicts, sep='\n')
    label = [x[0] for x in dicts]
    size = [x[1] for x in dicts]
    plt.axes(aspect=1)
    plt.pie(size, labels=label, labeldistance=1.1,
            autopct='%2.1f%%', shadow=True, startangle=90,
            pctdistance=0.8)
    plt.legend(loc='lower right', bbox_to_anchor=(1.3, 0))
    plt.show()


if __name__ == "__main__":
    show()
