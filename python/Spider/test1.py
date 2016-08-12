# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re

def urllibTest():
    url = "http://www.baidu.com"

    print "第一种方法"
    response1 = urllib2.urlopen(url)
    print response1.getcode()
    print len((response1).read())

    print "第二种方法"
    request = urllib2.Request(url)
    request.add_header("user-agent", "Mozilla/5.0")
    response2 = urllib2.urlopen(request)
    print response2.getcode()
    print len((response2).read())

    print "第三种方法"
    # cj = cookielib.CookieJar()
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    # urllib2.install_opener(opener)
    response3 = urllib2.urlopen(request)
    print response3.getcode()
    # print cj
    print len((response3).read())

def testFor():
    for i in range(10):
        print i

def testBeatu():
    htmlTest = "http://www.baidu.com"
    response1 = urllib2.urlopen(htmlTest)
    testHtml = response1.read()
    # print testHtml
    soup = BeautifulSoup(testHtml, "html.parser", from_encoding='utf-8')
    print "获取所有的链接"
    links = soup.find_all('a')
    print links
    for link in links:
        print link.name, link['href'], link.get_text()

    print "tieba"
    link_node = soup.find('a', href = "http://tieba.baidu.com")
    print link_node.name, link_node['href'], link_node.get_text()

    print "正则"
    link_node = soup.find('a', href = re.compile(r"more"))
    print link_node.name, link_node['href'], link_node.get_text()

    print "获取段落p文字"
    p_node = soup.find('a', class_="toindex")
    print p_node.name, p_node.get_text()

if __name__ == "__main__":
    # urllibTest()
    # print bs4
    testBeatu()