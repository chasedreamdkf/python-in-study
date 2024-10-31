# ------------      -------    --------    -----------    -----------
# @File       : 6.4.2 文本分析实验模板.py    
# @Contact    : vasp@qq.com
# @Copyright  : 2018-2025, Wuhan University of Technology
# @Modify Time: 2021/4/27 12:06
# @Author     : 赵广辉
# @Version    : 1.0
# @License    : 仅限用于Python程序设计基础实践教程(赵广辉,高等教育出版社)配套实验
# ------------      -------    --------    -----------    -----------
import string


def judge(method, txt):
    """
    @ 参数 method  字符串，值为'统计字符'、'统计单词'、'维吉尼亚加密'、'维吉尼亚解密'、'摩斯密码加密'
    @ 参数 text 字符串，可为明文也可以是密文
    接收一个字符串method为参数，根据参数值调用不同函数实现对文本的加密和解密。
    method 值为 '统计字符'时，统计并输出文本中不同类型字符的数量并输出。
    method 值为 '统计单词'时，统计并输出文本中单词的数量。
    method 值为 '首字符'时，将所有单词的首字符提取出来拼接为一个字符串输出。
    method 值为 '凯撒加密'时，再输入一个单词做为密钥发生器，用于计算偏移量，对文件中的内容进行加密并输出。
    若为其他输入，输出'输入错误'。
    """
    if method == '统计字符':
        classify = classify_char(text)
        print('大写字母{}个,小写字母{}个,数字{}个,空格{}个,其他{}个'.format(*classify))
    elif method == '统计单词':
        word_lst = word_list(text)         # 单词的列表
        words_counts = number_of_words(word_lst)
        print(f'共有{words_counts}单词')
    elif method == '首字符':
        word_lst = word_list(text)         # 单词的列表
        new_str = first_letter(word_lst)
        print(f'拼接的字符串是{new_str}')
    elif method == '凯撒加密':
        key = input()                       # 输入一个用于计算偏移量的单词
        offset = cal_offset(key)            # 计算偏移量
        print(caesar_cipher(text, offset))  # 加密
    else:
        print('输入错误')


def read_file(file):
    """接收文件名为参数，读取文件中的数据到字符串中，返回这个字符串。
    @ 参数 file： 文件名，字符串类型
    """
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()                 # 读取文件中的内容为一个字符串


def classify_char(txt):
    """接收字符串为参数，依序返回大写字母、小写字母、数字、空格、和其他字符数量，元组类型。
    @ 参数 txt： 字符串类型
    # >>> txt = 'Strive to make every day joyful and meaningful, not for others, but for myself.'
    # >>> classify_char(txt)
    # (1, 62, 0, 13, 3)
    # >>> txt = 'I am a student.'
    # >>> classify_char(txt)
    # (1, 10, 0, 3, 1)
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def word_list(txt):
    """接收字符串为参数，用空格替换字符串中所有标点符号，根据空格将字符串切分为列表。
    返回值为元素为单词的列表。
    @ 参数 txt： 字符串类型
    >>> s = 'Strive to make every day joyful and meaningful, not for others, but for myself.'
    >>> word_list(s)
    ['Strive', 'to', 'make', 'every', 'day', 'joyful', 'and', 'meaningful', 'not', 'for', 'others', 'but', 'for', 'myself']
    >>> s = 'I am a student.'
    >>> word_list(s)
    ['I', 'am', 'a', 'student']
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def number_of_words(ls):
    """接收一个以单词为元素的列表为参数，返回列表中单词数量，返回值为整型。
    @ 参数 ls： 列表类型
    >>> lst = ['I', 'am', 'a', 'student']
    >>> number_of_words(lst)
    4
    >>> lst = ['Strive', 'to', 'make', 'every', 'day', 'joyful', 'and', 'meaningful', 'not', 'for', 'others', 'but', 'for', 'myself']
    >>> number_of_words(lst)
    14
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def first_letter(ls):
    """接收一个以单词为元素的列表为参数，将列表中每个单词的首字符提取出来，合并为一个字符串，
    返回这个字符串。
    @ 参数 ls： 列表类型
    >>> lst = ['I', 'am', 'a', 'student']
    >>> first_letter(lst)
    'Iaas'
    >>> lst = ['Strive', 'to', 'make', 'every', 'day', 'joyful', 'and', 'meaningful', 'not', 'for', 'others', 'but', 'for', 'myself']
    >>> first_letter(lst)
    'Stmedjamnfobfm'
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def cal_offset(key_word):
    """接收一个字符串为参数，计算字符串中所有字符的Unicode值的和，将其再对9取模的结果作为偏移
    量，返回这个偏移量，整型。
    为保证结果的分散性好，建议用月份名字单词。
    @ 参数 key_word：字符串
    >>> cal_offset('March')
    5
    >>> cal_offset('May')
    7
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def caesar_cipher(text, offset):
    """接收一个字符串为参数，采用字母表和数字中后面第offset个字符代替当前字符
    的方法对字符串中的字母和数字进行替换，实现加密效果，返回值为加密的字符串。
    @参数 text：明文文本，字符串
    @参数 offset：偏移量，整型
    例如：2019 abc 替换为5342 def
    >>> txt = 'Attack on Pearl Harbor on December 7, 1941'
    >>> offset = 7
    >>> caesar_cipher(txt, offset)
    'Haahjr vu Wlhys Ohyivy vu Kljltily 4, 8618'
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


if __name__ == '__main__':
    filename = input()          # 输入要处理的文件名
    methods = input()           # 输入要进行的操作
    text = read_file(filename)  # text为读文件获得的字符串
    judge(methods, text)        # 调用函数，输出处理结果
