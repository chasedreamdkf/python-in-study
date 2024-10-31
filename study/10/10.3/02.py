import matplotlib.pyplot as plt

labels = ['Python', 'C++', 'C', 'Java', 'C#', 'JavaScript', 'Others']
sizes = [15.39, 10.03, 9.23, 8.40, 6.65, 3.32, 46.98]
explode = (0.1, 0, 0, 0, 0, 0, 0)
plt.axes(aspect=1)
plt.pie(sizes, explode, labels=labels, labeldistance=1.1, autopct='%2.1f%%', shadow=True,
        startangle=90, pctdistance=0.8)
plt.legend(loc='lower right', bbox_to_anchor=(1.3, 0))
plt.savefig('code_language_heat.jpg')
plt.show()
