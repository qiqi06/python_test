#coding:utf-8
#!/usr/bin/python
__author__ = 'fan'

import urllib2
import re


#将分析的过程封装成一个函数
def reptile(url1):

    url2, my_date = fun_url(url1)
    #保存网页地址
    page_url = url2.rstrip("index.html")
    # print page_url
    #print url2
    print my_date
    print ''
    #将完整的报表地址url2读取到内置函数read_html中
    read_html2 = urllib2.urlopen(url2)
    content2 = read_html2.read()
    pattern1 = re.compile("(192\.168\.[1-3]\d.\d{1,2})</a></td><td .*?>.*?</td><td .*?>(\d.\d{1,2}G)")
    items1 = re.findall(pattern1, content2)
    if items1:
        for i in items1:
            print i
        #i[0]获得ip地址
        savePage(page_url, i[0])
        makeIp(i[0])

    #应用正则表达式匹配IP与流量
    pattern2 = re.compile("(192\.168\.[1-3]\d.\d{1,2})</a></td><td .*?>.*?</td><td .*?>(\d*.\d*M)")
    items2 = re.findall(pattern2, content2)

    #出错可调试
    # print items2
    if items2:
    #打印流量排名的前五个IP和对应流量
        for i in range(5):
            int1 = float(items2[i][1].strip('M'))
            #print int1
            #如果大于流量定值则记录下来
            if int1> 600:
                print items2[i]
                savePage(page_url, items2[i][0])
                makeIp(items2[i][0])
            else:
                pass
                #print "None"

#根据日期获得完整报表地址
def fun_url(url1):
    #将参数url1的地址读取到内置函数read_html中
    read_html = urllib2.urlopen(url1)
    #将报表内容读取到变量content中
    content = read_html.read()

    #出错可以用print调试
    #print content

    #应用正则表达式匹配日期地址，因为每天的报表地址随日期变化
    pattern = re.compile("201\d\w{3}\d{2}-201\d\w{3}\d{2}/index.html")
    items = re.findall(pattern, content)

    #出错可调试
    # print items

    #应用正则表达式匹配时间地址，因为每天的报表地址随日期变化
    pattern2 = re.compile("\w*\s\d*\s\d{2}:\d{2}:\d{2}")
    items2 = re.findall(pattern2, content)
    # print items2

    for item in items:
    # print item
        #组装成正确的报表日期地址
        url2 = str(url1) + str(item)
        #出错可调试
        # print url2
        return url2, items2

#保存超量网页函数
#page_url  为公共网页地址
def savePage(page_url, ip):
    ip2 = str(ip).replace('.', '_')
    # print ip2
    page_url2 = page_url + ip2 + "/" + ip2 + ".html"
    # print page_url2
    read_html = urllib2.urlopen(page_url2)
    content2 = read_html.read()
    dir_file = time1(ip2)
    # print dir_file
    #2.4不认with open
    """
    with open(dir_file, "w") as f:
        f.write(content2)
"""
    f = open(dir_file, "w")
    f.write(content2)
    f.close

def time1(ip2):
    #获取当前时间
    import datetime
    now1 = datetime.datetime.now()
    now2 = now1.strftime("%Y-%m-%d(%H)")
    # print now2
    #now3 = "e:\\test_html\\" + now2 + ip2 + ".html"
    now3 = "/var/www/html/test/log/" + now2 + ip2 + ".html"
    return now3

#make ip for zhanglei`s scrip 
#为张雷的脚本提供ip

def makeIp(ip):
    dir_file = "/var/www/html/test/test_ip"
    f = open(dir_file, "w")
    f.write(ip)
    f.close 

def hua():
    for i in range(20):
        print "#",
    #主函数，运行程序必备

if __name__ == "__main__":
    #定义一个流量报表的网络地址，我们用这个网络地址做分析
    url1 = "http://192.168.24.59/anhour/"
    reptile(url1)
    hua()
