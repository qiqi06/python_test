#coding: utf-8
import requests
from bs4 import BeautifulSoup
import os
import urllib2
import cookielib

# res = requests.get('http://jandan.net/ooxx')
# # print res.text
# html = BeautifulSoup(res.text, "html.parser")
# print html
# print html.prettify()

# print html.a
# print html.a.string

#获取文档结构函数
def get_url(my_url):
    filename= 'cookie.txt'
    # res = requests.get(url)
    # 加入文件头
    send_headers = {

        # 'Host': 'static.duoshuo.com',
        'Host': 'jandan.net',
        # 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;WOW64; rv:47.0) Gecko/20100101 Firefox/37.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Referer':'http: // jandan.net / ooxx',
        'Pragma': 'no-cache'
    }
    # send_headers ={
    # 'Host': 'cdn.jandan.net',
    #     # 'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16',
    #     'User-Agent':'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 50.0.2661.102 Safari / 537.36',
    #     'Content-Type':'application/x-www-form-urlencoded',
    #     'Cache-Control':'no-cache',
    #     'Connection':'Keep-Alive'
    # }
    # send_headers = {
    #     'Host': 'jandan.net',
    #     'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
    #     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16'}
    # send_headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    #判断Cookie是否存在
    #没有存在
    if not os.path.exists(filename):
        cookie = cookielib.MozillaCookieJar(filename)
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        cookie.save(ignore_discard=True, ignore_expires=True)
    #存在
    else:
        cookie = cookielib.MozillaCookieJar(filename)
        cookie.load(filename, ignore_discard=True, ignore_expires=True)
        #创建request
        request1 = urllib2.Request(url=my_url, headers=send_headers)
        # print request1
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        try:
            # response1 = urllib2.urlopen(request1, timeout=5)
            response1 = opener.open(request1)
            # for item in cookie:
            #     print item
            print cookie
            # print response1.info()
            res = response1.read()
            html = BeautifulSoup(res, "html.parser")
            next_url = html.find('a', {'class': 'previous-comment-page'}).get('href')
            #返回网页内容和下一个地址
            return html, next_url
        except urllib2.URLError, e:
            print e.reason
            print e.code



#保存图片函数
def save_image(html, path):
    #获取网页内容
    index = 0
    for link in html.find_all('a',{'class': 'view_img_link'}):
        # print link
        # print link.get("href")
        # 取片内容   # print requests.get(link.get('href')).content()
        # print link.get('href')[-3:0]
        # print link.get('href')[len(link.get('href'))-3: len(link.get('href'))]
        # print link.get('href')

        #图片保存
        with open('./{}/{}.{}'.format(path, index, link.get('href')[-3:]), "wb") as jpg:
            jpg.write(requests.get(link.get('href')).content)
            index +=1

#文件夹建立函数
def mk_dir(path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print u"新建了名字叫做",path,u'的文件夹'
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print u"名为",path,'的文件夹已经创建成功'
            return False


#循环获取函数
def loop_get(url, path, n = 1):
    import time
    import random

    #获取网页内容和下一个网页地址
    print url, path
    try:
        html, url2  = get_url(url)
        #下一个目录名
        path2 = url2[-13:-9]
        #先建立目录
        mk_dir(path)
        #保存地址图片
        save_image(html, path)
        print "下一页的地址是:", url2
        if n != 1:
            for i in range(n):
                #生成一个随机数
                random_num = random.randint(10, 30)
                #让程序延迟几秒
                time.sleep(random_num)
                print "延迟%s" %random_num
                mk_dir(path2)
                html, url2  = get_url(url2)
                save_image(html, path2)
                path2 = url2[-13:-9]
                # print path2
    except Exception as e:
        print e



#主函数
if __name__ == "__main__":
    # url = 'http://jandan.net/ooxx'
    url = "http://jandan.net/ooxx/page-2041#comments"
    path = '2041'
    loop_get(url, path, 50)
