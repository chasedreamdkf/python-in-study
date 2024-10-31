import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']


# 读文件，根据制表符'\t'将每行数据切分为列表再加入到列表中
def read_file(file: str) -> list:
    """@参数 file：文件名，字符串
    读文件，根据制表符'\t'将每行数据切分为列表再加入到列表中将数据映射为浮点数类型。
    返回值为二维列表，其中数据是浮点数类型。
    """
    ls = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            d = map(float, line.strip().split('\t'))
            ls.append(list(d))
    # print(*ls, sep='\n')
    return ls


def plot_band_a(band_data: list):
    """@参数 band_data：数据是浮点数的二维列表
    x值从0-1的变化数据为一组，读取一组绘制一条曲线。"""
    x, y = [], []
    for xy in band_data:
        x.append(xy[0])
        y.append(xy[1])
        if x[-1] == 1:
            plt.plot(x, y)
            x, y = [], []
    plt.title('能带曲线')
    plt.show()


def plot_band_b(band_data: list, m: float, n: float):
    """@参数 band_data：数据是浮点数的二维列表
    @参数 m, n：用户输入的x轴取值范围，例如 -5 5
    x值从0-1的变化数据为一组，读取一组绘制一条曲线"""
    x, y = [], []
    for xy in band_data:
        x.append(xy[0])
        y.append(xy[1])
        if x[-1] == 1:
            a = [c for c, d in zip(x, y) if m <= c <= n]
            b = [d for c, d in zip(x, y) if m <= c <= n]
            plt.plot(a, b)
            x, y = [], []
    plt.title('能带曲线')
    plt.show()


def bottom_top_band(band_data: list):
    """@参数 band_data：数据是浮点数的二维列表
    定位导价底和价带顶的坐标
    导带底为纵坐标大于0的部曲线最低点
    价带顶为纵坐标小于0 的曲线最高点，一般导带底与价带顶相对，即横坐标相同。"""
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def gap_of_band(bottom, top):
    """
    @参数 bottom：纵坐标大于0的部曲线最低点，浮点数
    @参数 top：纵坐标小于0 的曲线最高点，浮点数
    接收导带底和价带顶的数值，带隙为导带底和价带顶纵坐标之差，返回带隙值。
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def mark_peak():
    """绘制注释，在y值大于0的部分找到曲线最低点，标注'bottom of conduction band'
    在y值小于0的部分找到曲线最高点，标注'top of valence band'。
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def plot_band_c(band_data, m, n):
    """
    @参数 band_data：数据是浮点数的二维列表
    @参数 m, n：用户输入的x轴取值范围，例如 -5 5
    根据列表中的数据绘制曲线，x值从0-1的变化数据为一组，读取一组绘制一条曲线"""
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


if __name__ == '__main__':
    filename = 'band.txt'
    data = read_file(filename)
    plot_band_a(data)
    min_value, max_value = map(float, input('请输入两个数字: ').split())  # 输入数据范围
    if min_value > max_value:
        min_value, max_value = max_value, min_value
    plot_band_b(data, min_value, max_value)
    bottom_top = bottom_top_band(data)
    band_gap = gap_of_band(*bottom_top)
    plot_band_c(data, min_value, max_value)
    print('导带底坐标为')
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码
    # =======================================================

    print('价带顶坐标为')
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码
    # =======================================================

    print('此物质带隙为')
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码
    # =======================================================
