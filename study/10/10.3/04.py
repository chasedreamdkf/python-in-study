import pandas as pd
from math import fsum
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
athletes = pd.read_csv('2012-19sport.csv', encoding='utf-8').values.tolist()
year = int(input('请输入想要查询的年份: '))
print(*athletes, sep='\n')
###########################################################
# 该年度体育运动收入饼图
athletes = [x for x in athletes if x[-1] == year]
sports = set(x[-2] for x in athletes)
ls = []
for sport in sports:
    s = [float(x[2][1:-1]) for x in athletes if x[-2] == sport]
    income = fsum(s)
    ls.append((sport, income))

ls.sort(key=lambda x: x[1], reverse=True)
sizes = [y for x, y in ls]
other = fsum(sizes[-3:])
sizes = sizes[:-3]
sizes.append(other)
sports = [x for x, y in ls]
sports = sports[:-3]
sports.append('Others')
explode = [0 for i in sports]
plt.subplot(122)  # 分成1 * 2，用第2个画布
plt.title(str(year)+'年度体育运动收入饼图')
plt.pie(sizes, explode, labels=sports, labeldistance=1.1, autopct='%3.2f%%',
        startangle=-90, pctdistance=0.8)
plt.legend(loc='lower right', bbox_to_anchor=(1.2, 0))
###########################################################
# 总收入排行前十的运动员收入排行的柱形图
athletes.sort(key=lambda x: float(x[2][1:-1]), reverse=True)
athlete_top10 = athletes[:10]
athlete_names = [x[1] for x in athlete_top10]
athlete_income = np.array([float(x[2][1:-1]) for x in athlete_top10])
plt.subplot(121)
plt.title(str(year)+'年总收入排行前十的运动员收入排行的柱形图')
plt.hist(athlete_income, bins=len(athlete_names), color='g', edgecolor='b')
plt.show()
