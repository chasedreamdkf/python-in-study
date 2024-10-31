# ------------      -------    --------    -----------    -----------
# @File       : 9.4.1 词频统计实验模板.py    
# @Contact    : vasp@qq.com
# @Copyright  : 2018-2025, Wuhan University of Technology
# @Modify Time: 2021/4/27 22:07
# @Author     : 赵广辉
# @Version    : 1.0
# @License    : 仅限用于Python程序设计基础实践教程(赵广辉,高等教育出版社)配套实验
# ------------      -------    --------    -----------    -----------
# 1. 将文件中的英文部分提取出来，所有字母改为小写，将标点、符号替换为空格，以字符串类型返回。
# 2. 去除标点、符号，统计并返回其中单词数量和不重复的单词数量。
# 3. 统计并返回每个单词出现的次数返回值为字典类型，单词为键，对应出现的次数为值。
# 4. 输出出现次数最多的10 个单词及其出现次数。
# 5. 去除常见的冠词、代词、系动词和连接词后，输出出现次数最多的10个单词及其出现次数。
# 6. 绘制词云

import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def read_file(file):
    """
    @参数 file: 文件名，字符串类型
    接收文件名为参数，将文件中的内容读为字符串，只保留文件中的英文字母和西文符号，过滤掉中文，
    所有字符转为小写，将其中所有标点、符号替换为空格，返回字符串。
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def count_of_words(txt):
    """
    @参数 txt： 西文文本，字符串类型
    接收去除标点、符号的字符串，统计并返回其中单词数量和不重复的单词数量
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def word_frequency(txt):
    """
    @参数 txt： 西文文本，字符串类型
    接收去除标点、符号的字符串，统计并返回每个单词出现的次数
    返回值为字典类型，单词为键，对应出现的次数为值，即词频字典。
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def top_ten_words(frequency):
    """
    @ 参数 frequency：词频字典，字典类型
    接收词频字典，输出出现次数最多的10个单词及其出现次数
    """
    # 依据单词数量对字典键值对降序排序，结果为列表类型
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def top_ten_words_no_excludes(frequency):
    """
    @ 参数 frequency：词频字典，字典类型
    接收词频字典，去除常见的冠词、代词、系动词和连接词后，输出出现次数最多的10个单词及其出现次数，需排除的单词如下：
    excludes_words = ['a', 'an', 'the', 'i', 'he', 'she', 'his', 'my', 'we','or', 'is', 'was',
                      'do', 'and', 'at', 'to', 'of', 'it', 'on', 'that', 'her', 'c','in', 'you',
                      'had', 's', 'with', 'for', 't', 'but', 'as', 'not', 'they', 'be', 'were',
                      'so', 'our', 'all', 'would', 'if', 'him', 'from', 'no', 'me', 'could', 'when',
                      'there', 'them', 'about', 'this', 'their', 'up', 'been', 'by', 'out', 'did',
                      'have']
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def draw_cloud(frequency):
    """绘制词云，传入参数为词频，设定图片的宽度600，高度400，背景白色、字体最大值150、图片边缘为5。"""
    wc = WordCloud(max_words=80,              # 设置显示高频单词数量
                   width=600,                 # 设置图片的宽度
                   height=400,                # 设置图片的高度
                   background_color='White',  # 设置背景颜色
                   max_font_size=150,         # 设置字体最大值
                   margin=5,                  # 设置图片的边缘
                   scale=1.5)                 # 按照比例进行放大画布，如设置为1.5，则长和宽都是原来画布的1.5倍。
    wc.generate_from_frequencies(frequency)   # 根据文本内容直接生成词云
    plt.imshow(wc)                            # 负责对图像进行处理，并显示其格式，但是不能显示。
    plt.axis("off")                           # 不显示坐标轴
    wc.to_file('My Cheese.png')               # 词云保存为图片
    plt.show()                                # 显示图像


if __name__ == '__main__':
    filename = '../data/Who Moved My Cheese.txt'  # 文件名
    content = read_file(filename)  # 调用函数返回字典类型的数据
    amount_results = count_of_words(content)
    frequency_result = word_frequency(content)
    print('文章共有单词{}个，其中不重复单词{}个'.format(*amount_results))
    top_ten_words(frequency_result)
    print()
    frequency_no_excludes = top_ten_words_no_excludes(frequency_result)
    draw_cloud(frequency_no_excludes)
