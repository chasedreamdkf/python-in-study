import re

# pat = re.compile('aa')  # 创建匹配模式对象
# m = pat.search('ascaa')  # search内的字符串是被校验的内容
# print(m)

# 未创建模式对象
# n = re.search('aa', 'asdaa')  # 前面是规则， 后面是检验对象
# print(n)

# m = re.findall("[A-Z]+", 'ASDWFaaSSd')  # 以列表形式返回后面被检验对象符合前面规则的所有内容
# print(m)

# m = re.sub('a', 'A', 'abcdefasd')  # 在第三个字符串中找到a，用A替换
# print(m)
# 建议在正则表达式中，被比较的字符串前面加上r，使转义字符不生效
# eg: a = r"\aaabcs\"
