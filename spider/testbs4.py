from bs4 import BeautifulSoup

file = open('douban.html', 'rb')
html = file.read().decode('utf-8')
bs = BeautifulSoup(html, 'html.parser')

# 1. Tag 获取第一个指定标签及其内容
# print(type(bs.title.string))
# print(bs.a)
# print(bs.head)

# 2. NavigableString  标签里的内容(字符串)
# print(bs.a.attrs)  # 以字典的形式获取标签中的元素及对应的元素值

# 3. BeautifulSoup     表示整个文档

# 4. Comment      特殊的NavigableString， 输出内容不包括注释


# 文档搜索
# (1) find_all() 以列表形式返回所有查找的标签
# 字符串过滤：会查找与字符串完全匹配的内容
#t_list = bs.find_all('a')

# 正则表达式搜索:使用Search()方法来匹配内容
# import re
#
# t_list = bs.find_all(re.compile('a'))

# 方法(函数) : 传入一个函数， 根据函数要求来搜索 (了解)
# def name_is_exists(tag):
#     return tag.has_attr('name')
#
#
# t_list = bs.find_all(name_is_exists)
# print(t_list)

# 2. kwargs     参数
# t_list = bs.find_all(id="head")
# print(t_list)

# 3.text 参数
# 4.limit参数
# t_list = bs.find_all('a', limit=2)

# CSS选择器
# t_list = bs.select('title') # 标签查找
# t_list = bs.select('.mnav') # 类名查找
# t_list = bs.select('#u1')     # id 查找
# t_list = bs.select("a[class='bri']") # 属性查找
# t_list = bs.select("head>title")     # 子标签查找
# t_list = bs.select(".mnav ~ .bri")   # 兄弟节点查找
# print(t_list)
