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

#给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。
#如：st="00:00:00", et="00:00:10", 则输出10.
def test13():

    #解法2
    import datetime

    st=datetime.datetime.strptime(st,"%H:%M:%S")
    et=datetime.datetime.strptime(et,"%H:%M:%S")
    print (et-st).seconds

#给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
#回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".
def test14():

    print('YES' if [i for i in range(len(a)-n+1) if a[i:(i+n)] == a[i:(i+n)][::-1]] else 'NO')

#给你一个整数组成的列表L，按照下列条件输出：
# 若L是升序排列的,则输出"UP";
# 若L是降序排列的,则输出"DOWN";
# 若L无序，则输出"WRONG"。

def test15():
    #解法2
    if L == sorted(L):
        print 'UP'
    elif L[::-1] == sorted(L):
        print 'DOWN'
    else:
        print 'WRONG'

    #解法3
    print L == sorted(L) and 'UP' or L == (sorted(L)[::-1]) and 'DOWN' or 'WRONG'

# 给你一个整数列表L,判断L中是否存在相同的数字，
# 若存在，输出YES，否则输出NO。
def test16():
    L = [3, 3, 8, 3, 22, 3, 9, 19, 1, 83]
    print 'No' if len(L) == len(set(L)) else 'Yes'

#给你三个整数a,b,c,  判断能否以它们为三个边长构成三角形。
#若能，输出YES，否则输出NO。
def test17():
    #解法1
    print sorted([a,b,c])[0] + sorted([a,b,c])[1] > sorted([a,b,c])[2] and 'YES' or 'NO'

    #解法2
    a+b+c-max(a,b,c）*2>0  #太赞了 真是好办法


#十一假期,小P出去爬山,爬山的过程中每隔10米他都会记录当前点的海拔高度(以一个浮点数表示),
# 这些值序列保存在一个由浮点数组成的列表h中。回到家中，小P想研究一下自己经过了几个山峰，请你帮他计算一下，输出结果。
# 例如：h=[0.9,1.2,1.22,1.1,1.6,0.99], 将这些高度顺序连线，会发现有两个山峰，故输出一个2(序列两端不算山峰)
def test18():
    h=[0.9,1.2,1.22,1.1,1.6,0.99]
    print sum([1 for i in xrange(1, len(h) - 1) if h[i] > h[i - 1] and h[i] > h[i + 1]])

    #解法2
    sum = 0
    h=[0.9,1.2,1.22,1.1,1.6,0.99, 4, 1]
    for i in range(1, len(h)-1):
        #列表得从1开始
        if h[i] > h[i-1] and h[i] > h[i+1]:
            sum += 1
    print sum

#给以一个三角形的三边长a,b和c(边长是浮点数),请你判断三角形的形状。
# 若是锐角三角形，输出R,
# 若是直角三角形，输出Z，
# 若是钝角三角形，输出D，
# 若三边长不能构成三角形，输出W.

def test20():
    L = [a, b, c]
    L.sort()
    if L[0]+L[1] <= L[2]:
        print 'W'
    else:
        if L[0]*L[0] + L[1]*L[1] == L[2]*L[2]:
            print 'Z'
        elif L[0]*L[0]+ L[1]*L[1] > L[2]*L[2]:
            print 'R'
        else:
            print 'D'

    #解法2
    a,b,c = sorted([a,b,c])
    print a+b<c and 'W' or a*a + b*b - c*c < 0 and 'D' or a*a + b*b - c*c == 0 and 'Z'or 'R'

#给你两个正整数a(0 < a < 100000)和n(0 <= n <=100000000000)，计算(a^n) % 20132013并输出结果
def test21():
    print pow(a, n, 20132013)


#生活在当代社会，我们要记住很多密码，银行卡，qq，人人，微博，邮箱等等。小P经过一番思索之后，发明了下面这种生成密码方法：
# 给定两个正整数a和b, 利用a / b我们会到的一个长度无限的小数(若a / b不是无限小数，
# 比如1/2=0.5,我们认为0.5是0.5000000...，同样将其看做无限长的小数），小P将该小数点后第x位到第y位的数字
# 当做密码，这样，无论密码有多长，小P只要记住a,b,x,y四个数字就可以了，牢记密码再也不是那么困难的事情了。
# 现在告诉你a,b,x,y（0 < a,b <= 20132013, 0 < x <= y < 100000000000),请你输出密码。
# 例如：a = 1, b = 2, x = 1, y = 4, 则 a / b = 0.5000000..., 输出小数点后第1到4位数字，即5000
def test22():
    a = 1
    b = 2
    x = 1
    y = 4
    from __future__ import print_function
    list, ans, a = [], [], a%b
    while (a, b) not in list:
        list.append((a, b))
        if a < b:
            ans.append(0)
        else:
            ans.append(a // b)
            a = a % b
        a *= 10
    nolooplen = list.index((a, b))
    looplen = len(ans) - nolooplen
    # print(list, ans, nolooplen, looplen)
    for i in range(x, y + 1):
        if i < len(ans):
            print(ans[i], end='')
        else:
            print(ans[(i - nolooplen) % looplen + nolooplen], end='')
    print('')

# 给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个连续子序列，使其和最大，输出最大子序列的和。
# 例如，对于L=[2,-3,3,50]， 输出53（分析：很明显，该列表最大连续子序列为[3,50]).
def test23():
    #能够想到设计一个以第j处结束的子序列的最大和数组b[j]。这也是一种巧妙的遍历.

    # 设b[j]表示以a[j] 结尾的子序列的最大和。
    #        则b[j] = max(a[j] + b[j-1] , a[j]) ，

    # 代码如下：
    L=[2,-3,3,50]
    B=[0 for i in range(len(L))]B[0]=L[0]
    for i in range(1,len(L)):
        B[i]=max(B[i-1]+L[i],L[i])
    print max(B)

# 给你直角三角形的两个直角边的边长a,b,请你求出其斜边边长，结果保留小数点后三位小数。
# 如a=3, b =4, 则输出5.000。
def test24():
    import math
    a, b = 3, 4
    c = math.sqrt(pow(a, 2) + pow(b, 2))
    print '%.3f' %c

# 给你两个整数a和b（-10000<a,b<10000），请你判断是否存在两个整数，他们的和为a，乘积为b。
# 若存在，输出Yes,否则输出No
# 例如：a=9,b=15, 此时不存在两个整数满足上述条件，所以应该输出No。
def test25():
    import random
    a = random.randint(-10000, 10000)
    b = random.randint(-10000, 10000)
    a, b = sorted([a, b])
    print a, b

# Py从小喜欢奇特的东西，而且天生对数字特别敏感，一次偶然的机会，他发现了一个有趣的四位数2992，
# 这个数，它的十进制数表示，其四位数字之和为2+9+9+2=22，它的十六进制数BB0，其四位数字之和也为22，
# 同时它的十二进制数表示1894，其四位数字之和也为22，啊哈，真是巧啊。
# Py非常喜欢这种四位数，由于他的发现，所以这里我们命名其为Py数。
# 现在给你一个十进制4位数n，你来判断n是不是Py数，若是，则输出Yes，否则输出No。
# 如n=2992，则输出Yes； n = 9999，则输出No

def test26():
    a = 0
    tmp = n
    while tmp:
	    a += tmp % 12
	    tmp //= 12

    b = 0
    tmp = n
    while tmp:
        b += tmp % 10
        tmp //= 10

    c = 0
    tmp = n
    while tmp:
        c += tmp % 16
        tmp //= 16

    if a == b and b == c:
        print("Yes")
    else:
        print("No")

    #解法2
    def conv(n,m):
    temp = []
    while n != 0:
         temp.append(n % m)
         n = n / m
    return sum(temp)

    print conv(n,16) == conv(n,12) == conv(n,10) and 'Yes'or 'No'


#
def test27():
    def list_test(x):
        a = b = 1
        for i in xrange(x):
            yield a
            a , b = b, a + b

    list1 = []
    for i in list_test(n+1):
        list1.append(i)
    print list1[n - 1] % 20132013

# 有一楼梯共n级，刚开始时你在第一级，若每次只能跨上一级或二级，要走上第n级，共有多少种走法？
# 现在给你一个正整数n（0<n<40),请你输出不同的走法数。
# 如n=2,则输出1（你只有一种走法，走一步，从第一级到第二级）

def test28():
    pass

# 给你一个十进制数a，将它转换成b进制数,如果b>10,用大写字母表示（10用A表示，等等）
# a为32位整数，2 <= b <= 16
# 如a=3,b = 2, 则输出11

def test29():
    a = 3
    b = 16

    #解法1
    sign = '0123456789ABCEDF'
    ans = ""
    flag = 0
    if a < 0:
        flag = 1
        a = -a

    while a > 0:
        ans += sign[a%b]
        a //= b
    if flag:
        ans += '-'
    print(ans[::-1])


    #解法2
    d = '0123456789ABCEDFGHIJKLMNOPQRSTUVWXYZ'
    def f(x,y):
        s = []
        while x>=y:
            s.append(x%y)
            x /=y
        s.append(x)
        return ''.join([d[c] for c in s[::-1]])

    print (a<0 and '-' or '')+f(abs(a),b)






if __name__ == '__main__':
    # test01()
    # test02()
    # test05()
    # test06()
    # test07()
    # test08()
    # test09()
    # test10()
    # test11()
    pass