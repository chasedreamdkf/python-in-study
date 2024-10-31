import urllib.request

# 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  # 对获取到的网页源码进行utf-8解码

# 获取一个post请求
# import urllib.parse
# # 封装post数据， 向浏览器发送请求
# d = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf_8")
# r = urllib.request.urlopen("http://httpbin.org/post", data=d)
# print(r.read().decode('utf-8'))

# 超时处理
# try:
#     r = urllib.request.urlopen("http://httpbin.org/get", timeout=1)  # timeout限定访问时间，判断是否超市
#     print(r.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")


# r = urllib.request.urlopen("http://httpbin.org/get")
# print(r.status) # 状态码
# print(r.getheaders())

# 伪装自己是浏览器，避开反爬虫机制
url = "https://movie.douban.com/top250?start="
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
# d = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=d, headers=header, method="POST")
req = urllib.request.Request(url=url, headers=header)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))






















