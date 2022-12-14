#!/usr/bin/env python
import urllib.request
import urllib.parse
#测试网址：http://httpbin.org/post

#定义一个字典参数
data_dict = {"username":"","password":""}

#使用urlencode将字典参数序列化成字符串
data_string = urllib.parse.urlencode(data_dict)
#将序列化后的字符串转换成二进制数据，因为post请求携带的是二进制参数
last_data = bytes(data_string, encoding='utf-8')

#如果给urlopen这个函数传递了data这个参数，那么它的请求方式则不是get请求，而是post请求
response = urllib.request.urlopen("http://p.nju.edu.cn/portal_io/login", data=last_data)

#我们的参数出现在form表单中，这表明是模拟了表单的提交方式，以post方式传输数据
print(response.read().decode('utf-8'))
