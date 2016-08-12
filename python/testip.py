#-*-coding: UTF-8 -*-
#!/usr/bin/python

#利用生成器生成实验性IP数据文件，用于查找替换
def writeIP(dir1):
    with open(dir1, 'a') as f:
        for i in testIP():
            f.write(i)

#创建一个生成器
def testIP():
    for i in range(10):
        yield "192.168.1.%s 00:00:00:00:00:00\n" %i

#生成器读取
def testIP2():
    for i in testIP():
        return i

#查找替换主函数
def changeIP(test_ip, dir1_file):
    dir2_file = r"d:\python\test\testip2.txt"
    test_mac = " 00:ee:ee:ee:55:cc"
    print test_ip
    test_ip2 = test_ip + test_mac
    print test_ip2
    with open(dir1_file, "r") as f1:
        with open(dir2_file, "w") as f2:
            for line in f1.readlines():
                # f2.write(line)
                f2.write(line.replace(test_ip, test_ip2))
                # f2.write(line.replace("hello", "qiqi"))
            

def changeIP2(test_ip):
    dir2_file = r"d:\python\test\testip.txt"
    with open(dir2_file, "r") as f:
        for line in f.readlines():
            # print line
            print line.replace(test_ip, "qiqi06")
            
        # f.write(d)




if __name__ == "__main__":
    #指定生成实验性ip数据文件位置
    dir1_file = r"d:\python\test\testip.txt"
    
    #执行生成实验IP数据文件
    # writeIP(dir1_file)

    #测试生成器生成的内容
    # testIP2()

    #指定查找的IP
    test_ip = "192.168.1.6"
    # changeIP2(test_ip)
    changeIP(test_ip, dir1_file)
    # print test_ip.replace("192.168.", "qiqi")