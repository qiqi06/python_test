#coding:utf-8
__author__ = 'fan'

import urllib2
import re


#�������Ĺ��̷�װ��һ������
def reptile(url1):

    url2, my_date = fun_url(url1)
    #print url2
    print my_date
    print ''
    #�������ı����ַurl2��ȡ�����ú���read_html��
    read_html2 = urllib2.urlopen(url2)
    content2 = read_html2.read()

    pattern1 = re.compile("(192\.168\.[1-3]\d.\d{1,2})</a></td><td .*?>.*?</td><td .*?>(\d.\d{1,2}G)")
    items1 = re.findall(pattern1, content2)
    if items1:
        for i in items1:
            print i

    #Ӧ��������ʽƥ��IP������
    pattern2 = re.compile("(192\.168\.[1-3]\d.\d{1,2})</a></td><td .*?>.*?</td><td .*?>(\d*.\d*M)")
    items2 = re.findall(pattern2, content2)

    #����ɵ���
    # print items2
    if items2:
    #��ӡ����������ǰ���IP�Ͷ�Ӧ����
        for i in range(5):
            int1 = float(items2[i][1].strip('M')) 
            #print int1
            if int1> 500:
                print items2[i]
            else:
                pass
                #print "None"
#�������ڻ�����������ַ
def fun_url(url1):
    #������url1�ĵ�ַ��ȡ�����ú���read_html��
    read_html = urllib2.urlopen(url1)
    #���������ݶ�ȡ������content��
    content = read_html.read()

    #���������print����
    #print content

    #Ӧ��������ʽƥ�����ڵ�ַ����Ϊÿ��ı����ַ�����ڱ仯
    pattern = re.compile("201\d\w{3}\d{2}-201\d\w{3}\d{2}/index.html")
    items = re.findall(pattern, content)

    #����ɵ���
    # print items

    #Ӧ��������ʽƥ��ʱ���ַ����Ϊÿ��ı����ַ�����ڱ仯
    pattern2 = re.compile("\w*\s\d*\s\d{2}:\d{2}:\d{2}")
    items2 = re.findall(pattern2, content)
    # print items2

    for item in items:
    # print item

        #��װ����ȷ�ı������ڵ�ַ
        url2 = str(url1) + str(item)

        #����ɵ���
        # print url2
        return url2, items2

def hua():
    for i in range(20):
        print "#", 
    #�����������г���ر�
if __name__ == "__main__":
    #����һ����������������ַ����������������ַ������
    url1 = "http://192.168.24.59/anhour/"
    reptile(url1)
    hua()
