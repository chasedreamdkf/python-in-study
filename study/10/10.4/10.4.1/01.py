# X射线衍射曲线
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']


def read_file(filename: str):
    ls = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            ls.append(line.strip().split())
    data_list = [[float(x[0]), float(x[1])] for x in ls[1:]]
    # print(*data_list, sep='\n')
    return data_list


def plot_xrd_a(data_list: list):
    """
    @参数 data_list：读文件获得的数据列表，列表类型
    接收一个列表为参数，列表的元素为包含x和y数据的列表
    绘制问题1的曲线。
    """
    x = [a[0] for a in data_list]
    y = [a[1] for a in data_list]
    plt.plot(x, y)
    plt.savefig('01_1.jpg')
    plt.show()


def plot_xrd_b(data_list: list):
    """
    @参数 data_list：读文件获得的数据列表，列表类型
    接收一个列表为参数，列表的元素为包含x和y数据的列表。
    绘制问题2的曲线。
    """
    x = [a[0] for a in data_list]
    y = [a[1] for a in data_list]
    plt.title('X射线衍射图谱')
    plt.plot(x, y, color='r')
    plt.axhline(0, 0, 1, linestyle='--', color='r')
    plt.axvline(0, 0, 1, linestyle='--', color='b')
    plt.xlabel('2d')
    plt.ylabel('Intensity')
    plt.savefig('01_2.jpg')
    plt.show()


def top_five_peak(data_list: list) -> list:
    """
    @参数 data_list：读文件获得的数据列表，列表类型
    接收数据列表为参数，返回纵坐标值最大的5个峰的坐标的列表，降序排序。
    """
    ls = sorted(data_list, key=lambda x: x[1], reverse=True)
    ls = [tuple(x) for x in ls[:5]]
    print('top_peak:', *ls, sep='\n')
    return ls


def mark_peak(sort_of_ls: list):
    """
    @参数 sort_of_ls：排序后的数据列表，列表类型
    接收排序的数据，在指定的坐标点加注释。注释标记点相对横坐标偏移+30，纵坐标等高，
    注释文本为峰高，即y 值。
    """
    for x, y in sort_of_ls:
        plt.annotate(f'{y}', xy=(x, y), xytext=(+30, 0),
                     textcoords='offset points', fontsize=12,
                     arrowprops=dict(arrowstyle='->',
                                     connectionstyle='arc3, rad=.2'))


def plot_xrd_c(data_list: list, sort_of_ls: list):
    """
    @参数 data_list：读文件获得的数据列表，列表类型
    @参数 sort_of_ls：排序后的数据列表，列表类型
    接收一个元组为参数，元组的元素为包含x和y数据的列表
    绘制问题3的曲线。
    """
    x = [a[0] for a in data_list]
    y = [a[1] for a in data_list]
    plt.title('X射线衍射图谱')
    plt.plot(x, y, color='r')
    mark_peak(sort_of_ls)
    plt.axhline(0, 0, 1, linestyle='--', color='r')
    plt.axvline(0, 0, 1, linestyle='--', color='b')
    plt.xlabel('2d')
    plt.ylabel('Intensity')
    plt.savefig('01_3.jpg')
    plt.show()


def plot_xrd_d(data_list: list, sort_of_ls: list):
    """
    @参数 data_list：读文件获得的数据列表，列表类型
    @参数 sort_of_ls：排序后的数据列表，列表类型
    接收一个元组为参数，元组的元素为包含x和y数据的列表
    绘制问题4的曲线。
    """
    plt.subplot(211)
    x = [a[0] for a in data_list if 5 <= a[0] <= 25]
    y = [a[1] for a in data_list if 5 <= a[0] <= 25]
    plt.title('X射线衍射图谱')
    plt.plot(x, y, color='r')
    mark_peak(sort_of_ls)
    plt.axhline(0, 0, 1, linestyle='--', color='r')
    plt.axvline(5, 0, 1, linestyle='--', color='b')
    plt.xlabel('2d')
    plt.ylabel('Intensity')
    plt.subplot(223)
    x = [a[0] for a in data_list if 6.7 <= a[0] <= 7.0]
    y = [a[1] for a in data_list if 6.7 <= a[0] <= 7.0]
    plt.plot(x, y, color='g')
    plt.subplot(224)
    x = [a[0] for a in data_list if 9.5 <= a[0] <= 10.0]
    y = [a[1] for a in data_list if 9.5 <= a[0] <= 10.0]
    plt.plot(x, y)
    plt.savefig('01_4.jpg')
    plt.show()


if __name__ == '__main__':
    file = 'XRD_AFO.txt'  # 带路径文件名
    file_to_list = read_file(file)
    plot_xrd_a(file_to_list)
    plot_xrd_b(file_to_list)
    top_peak = top_five_peak(file_to_list)
    plot_xrd_c(file_to_list, top_peak)
    plot_xrd_d(file_to_list, top_peak)
