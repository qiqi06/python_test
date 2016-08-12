#coding: utf-8

#给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','链接，如‘1,2,3'。
def test01():
    a={1:1, 2:2, 3:3}
    #我做的
    test = [str(x) for x in a.keys()]
    print ','.join(test)
    #解二
    print ','.join(str(key)for key in a)

#给你一个字符串 a， 输出字符奇数位置的字符串。如a=‘12345’，则输出135。
def test02():
    a = '12345'
    print a[::2]

#输出100以内的所有素数，素数之间以一个空格区分
def test03(n):
    for i in range(2, n):

        if( n%i == 0):

            return False

    return True

print(" ".join(str(i) for i in filter(test03, range(2, 101))))

def test04():
    a, b  = 3, 5
    print a * b, 2 * (a + b)

#给你一个list L, 如 L=[0,1,2,3,4], 输出L的中位数（若结果为小数，则保留一位小数）。
def test05():
    L.sort()
    if len(L) % 2 == 0:
        res = L[len(L)/2]+L[len(L)/2-1]
        print res / 2.0
    else:
        print L[len(L)/2]

    #解法2
    L.sort()
    print L[len(L)/2] if len(L) % 2 != 0 else (L[len(L)/2-1] + L[len(L)/2])/2.0


'''
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
在中文大写方式中，0到10以及100、1000、10000被依次表示为：
    零壹贰叁肆伍陆柒捌玖拾佰仟万
以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1	壹圆
11	壹拾壹圆
111	壹佰壹拾壹圆
101	壹佰零壹圆
-1000	负壹仟圆
1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 打印出人民币大写表示.
注意：请以Unicode的形式输出答案。你可以通过decode("utf8")来将utf8格式的字符串解码为Unicode，例如你要输出ans = "零圆", print ans.decode("utf8").
Note：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。
'''
def test05():
    a = 32829322
    a = 1000000
    # a = -293783
    mylist=['零','壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','佰','仟','万','圆']

    ll=[]
    def func(aa):
        al=[]
        for i in range(len(aa)-1):
                al.append((mylist[int(aa[i])]+mylist[len(aa)-i+8]))

        al.append(mylist[int(aa[-1])])
        return al

    aa=list(str(a))
    if aa[0]=='-':
        ll+=['负']
        aa[:1]=[]
    if len(aa)<=4:
        ll+=func(aa)+['圆']
    else:

        ll+=func(aa[:-4])+['万']+func(aa[-4:])+['圆']


    pstring=''.join(ll)
    pstring=pstring.replace('零万', '万').replace('零仟', '零').replace('零佰', '零').replace('零拾', '零').replace('零零', '零').rstrip('零')
    print pstring

    print (u"负" if a < 0 else "") + "".join([(u"零壹贰叁肆伍陆柒捌玖"[int(v)] if i==0 or v!=u"0" or str(abs(a))[i-1]!=u"0" else "") +(u"拾佰仟万"[(len(str(abs(a)))-i-2)%4] if int(v)!=0 and len(str(abs(a)))!=i+1 else "") for i,v in enumerate(str(abs(a)))]).rstrip(u"零" if a!=0 else "")+u"圆"


#现在来练习一下发现爱的能力，给你一个字符串a,
# 如果其中包含"LOVE"（love不区分大小写)则输出LOVE，否则输出SINGLE。

def test06():
    import re
    a = 'dsjfslovEdd222'
    pattern = re.compile('love')
    fs = re.findall(pattern, a.lower())
    if fs:
        print 'LOVE'
    else:
        print 'single'

    #解法2
    print 'LOVE' if 'love' in a.lower() else 'SINGLE'



#给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。
#这里将字母表的z和a相连，如果超过了z就回到了a。例如a="cagy",b=3, 则输出 fdjb
def test07():
    a = 'abc'
    b = 25
    str = ''
    for i in a:
        str += chr(ord(i) + b)
    print str

    #解法2
    print(''.join([chr((ord(i)+b-ord('a'))%26+ord('a')) for i in a]))

    #解法3
    s = "abcdefghijklmnopqrstuvwxyz"
    print "".join(map(lambda c:s[(s.index(c)+b)%26], a))

#光棍们对1总是那么敏感，因此每年的11.11被戏称为光棍节。
#鄙人光棍几十载，光棍自有光棍的快乐。让我们勇敢面对光棍的身份吧，
#现在就证明自己：给你一个整数a，数出a在二进制表示下1的个数，并输出。
def test08():
    a = 922
    b = bin(a).replace('0b', '')
    print b
    print b.count('1')

    #解法2
    print(str(bin(a)).count('1'))

def test09():
    L = [1, 3, 7, 50]
    s = 1
    for i in L:
        s *= i
    print s
    #去除0
    r = int(str(s).strip('0')[-1])
    print r % 2


#给你两个正整数a和b， 输出它们的最大公约数。
def gcd_Stein(a, b):
    if a < b:
        a, b = b, a
    if (0 == b):
        return a
    if a % 2 == 0 and b % 2 == 0:
        return 2 * gcd_Stein(a/2, b/2)
    if a % 2 == 0:
        return gcd_Stein(a/2, b)
    if b % 2 == 0:
        return gcd_Stein(a, b/2)

    return gcd_Stein((a + b) / 2, (a - b) / 2)
s = gcd_Stein(15, 30)
print s

#最小公倍数
# 定义函数
def lcm(x, y):

    #  获取最大的数
    if x > y:
       greater = x
    else:
       greater = y

    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

    return lcm



#给你一个正整数列表 L, 如 L=[2,8,3,50], 输出L内所有数字的乘积末尾0的个数,
#如样例L的结果为2.(提示:不要直接相乘,数字很多,可能溢出)
def test10():

    #我做的错误
    L = [2, 8, 3, 50]
    s = 1
    for i in L:
        s*=i
    print s
    print str(s).count('0')

    #解法2
    c1, c2 = 0, 0
    for x in L:
        while x%2 == 0:
            x = x / 2
            c1 += 1
        while x%5 == 0:
            x = x / 5
            c2 += 1
    print min(c1,c2)


#一年有多少天，这是个大问题，很值得思考。现在给你一个年份year(year为四位数字的字符串，如"2008","0012"),
#你输出这一年的天数。如year="2013", 则输出365。
def test11():
    year = 2016

    import datetime
    print datetime.date((year), 12, 31).timetuple()[7]

#给你一个时间t（t是一个字典，共有六个字符串key(year,month,day,hour,minute,second),值为每个值为数字组成的字符串，
#如t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
#请将其按照以下格式输出， 格式:XXXX-XX-XX XX:XX:XX。如上例应该输出： 2013-09-30 16:45:02。
def test12():
    import datetime

    t = {'year': '2013', 'month': '9', 'day': '30', 'hour': '16', 'minute': '45', 'second': '2'}
    for k, v in t.items():
        t[k] = int(v)
    print t
    print datetime.datetime(t['year'],t['month'],t['day'],t['hour'],t['minute'],t['second']).strftime("%Y-%m-%d %X")

    #解法2
    import datetime
    for k, v in t.items():
        t[k] = int(v)
    print datetime.datetime(**t).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    # test01()
    # test02()
    # test05()
    # test06()
    # test07()
    # test08()
    # test09()
    test10()
    test11()