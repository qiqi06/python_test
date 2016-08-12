#-*-coding:utf-8-*-
#/usr/bin/python
import socket

#socke编程实现
def testBase():

    #获取本机的名称与IP地址
    myPcName = socket.gethostname()
    print "My pc name is %s" %myPcName
    myPcIp =  socket.gethostbyname(myPcName)
    print "My Ip is %s " %myPcIp

    #解析百度的ip地址
    baiduIP = socket.gethostbyname("www.baidu.com")
    print "Baidu IP is %s" %baiduIP

    #解析163地址
    wangyiIP = socket.gethostbyname("www.163.com")
    print "163 IP is %s" %wangyiIP

    #根据ip解析地址
    testIp = "112.100.100.100"
    mytestName = socket.gethostbyaddr(testIp)
    print mytestName

    #测试地址
    # mytest = socket.gethostbyname("")
    # print "mytest  is %s" %mytest


#客户端
def ClientSocket():
    host = socket.gethostname()
    #ip = socket.gethostbyname(host)
    port = 1235
    addr = (host, port)
    print addr 
    #创建一个socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)
    print s.recv(1024)
    for data in ['Michael', 'Tracy', 'Sarah']:
        # 发送数据:
        s.send(data)
        print s.recv(1024)
    s.send('exit')
    s.close()



if __name__ == "__main__":
    print "main of modle is running !"

#socket 编程
    ClientSocket()

else:
    print "modle is by running !"
