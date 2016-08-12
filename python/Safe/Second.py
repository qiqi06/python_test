#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
# Date: 2015/9/17
# Created by ���Եȴ�
# ���� http://www.waitalone.cn/
import sys, os
import urllib2

try:
    from lxml import html
except ImportError:
    raise SystemExit('\n[X] lxmlģ�鵼�����,��ִ��pip install lxml��װ!')


class SubMain():
    '''
    ��͸���������ռ�
    '''

    def __init__(self, submain):
        self.submain = submain
        self.url_360 = 'http://webscan.360.cn/sub/index/?url=%s' % self.submain
        self.url_link = 'http://i.links.cn/subdomain/'
        self.link_post = 'domain=%s&b2=1&b3=1&b4=1' % self.submain
        self.sublist = []

    def get_360(self):
        scan_data = urllib2.urlopen(self.url_360).read()
        html_data = html.fromstring(scan_data)
        submains = html_data.xpath("//dd/strong/text()")
        return self.sublist.extend(submains)

    def get_links(self):
        link_data = urllib2.Request(self.url_link, data=self.link_post)
        link_res = urllib2.urlopen(link_data).read()
        html_data = html.fromstring(link_res)
        submains = html_data.xpath("//div[@class='domain']/a/text()")
        submains = [i.replace('http://', '') for i in submains]
        return self.sublist.extend(submains)

    def scan_domain(self):
        self.get_360()
        self.get_links()
        return list(set(self.sublist))


if __name__ == '__main__':
    print '+' + '-' * 50 + '+'
    print '\t    Python ����������Ϣ�ռ�����'
    print '\t   Blog��http://www.waitalone.cn/'
    print '\t\t Code BY�� ���Եȴ�'
    print '\t\t Time��2015-09-17'
    print '+' + '-' * 50 + '+'
    if len(sys.argv) != 2:
        print '�÷�: ' + os.path.basename(sys.argv[0]) + ' ��������ַ'
        print 'ʵ��: ' + os.path.basename(sys.argv[0]) + ' waitalone.cn'
        sys.exit()
    domain = sys.argv[1]
    print u'����ү,�����ռ�������Ϣ,���Ժ�!\n'
    submain = SubMain(domain).scan_domain()
    print u'����ү,������������Ϣ [ %d ] ��!\n' % len(submain)
    with open(domain + '.txt', 'wb+') as domain_file:
        for item in submain:
            domain_file.write(item + '\n')
            print item
