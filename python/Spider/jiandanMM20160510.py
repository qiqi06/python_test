#-*-coding: utf-8-*-
import requests
from bs4 import BeautifulSoup
import os
import urllib2

# res = requests.get('http://jandan.net/ooxx')
# # print res.text
# html = BeautifulSoup(res.text, "html.parser")
# print html
# print html.prettify()

# print html.a
# print html.a.string

#获取文档结构函数
def get_url(my_url):
    # res = requests.get(url)
    #加入文件头
    send_headers = {
     'Host':'jandan.net',
     'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'Connection':'keep-alive'
    }
    # header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    request = urllib2.Request(url=my_url, headers=send_headers)
    response = urllib2.urlopen(request)
    res = response.read()
    # print res
    html = BeautifulSoup(res, "html.parser")
    next_url = html.find('a', {'class': 'previous-comment-page'}).get('href')
    return html, next_url

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
            print u"偷偷新建了名字叫做",path,u'的文件夹'
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print u"名为",path,'的文件夹已经创建成功'
            return False


#循环获取函数
def loop_get(url, path, n = 1):

    #获取网页内容和下一个网页地址
    print url, path
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
            mk_dir(path2)
            html, url2  = get_url(url2)
            save_image(html, path2)
            path2 = url2[-13:-9]
            # print path2



#主函数
if __name__ == "__main__":
    # url = 'http://jandan.net/ooxx'
    url = "http://jandan.net/ooxx/page-1967#comments"
    path = '1967'
    loop_get(url, path, 4)
