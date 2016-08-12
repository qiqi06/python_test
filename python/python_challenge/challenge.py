#coding: utf-8

#第0关
def level0():
    print 2 ** 38

#第1关
def level1():
    w = ''
    string1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    string2 = "map"
    for char in string2:
        if char.isalpha() and char not in "yz":
            new_char = chr(ord(char) + 2)
            w += new_char
        if char == 'y':
            w += 'a'
        if char == 'z':
            w += 'b'
    print w


#第2关
def level2():
    w = ''
    with open('level2.txt') as f:
        # print f.read()
        for char in f.read():
            if char.isalpha():
                w += char
        print w

#第3关
def level3():
    import re

    w = ''
    pattern = '[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]'

    with open('level3.txt') as f:
        # print f.read()
        tmp = re.findall(pattern, f.read())
        for march in  tmp:
            w += march[4]
        print w

#第4关
def level4():
    import urllib2
    import re
    r=re.compile(r'(\d+)$')
    nextnothing='8022'
    i=0
    while(1):
       try:
           f=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'% nextnothing)
           result=f.read()
           f.close()
           print result
           oldnextnothing=nextnothing
           nextnothing=r.search(result).group()
           i+=1
       except:
           nextnothing=oldnextnothing

#第5关
#level5
def level5():
    import urllib2
    import cPickle as pickle
    import os

    my_url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    file1 = urllib2.urlopen(my_url)
    file_name = 'level5.txt'
    if os.path.exists(file_name):
        print 'level5.txt is exist!'
        file_pickle = pickle.load(open(file_name))
        print file_pickle
        for item in file_pickle:
            print  ''.join(map(lambda p: p[0] * p[1], item ))

    else:
        with open('level5.txt', 'w') as f:
            f.write(file1.read())

#level6
def level6():
    import zipfile
    import re

    w = []
    r = re.compile(r'(\d+)$')
    file_list = zipfile.ZipFile('channel.zip')
    # for name in file_list.namelist():
    #     print name
    #
    print file_list.read('readme.txt')
    file_name1 ='90052.txt'
    try:
        while True:
            result = file_list.read(file_name1)
            print result
            w.append( file_list.getinfo(file_name1).comment)
            file_name1 = r.search(result).group() + '.txt'

    except Exception as ex:
        print ex

    print ''.join(w)

#level7
#灰度
def level7():
    import urllib2
    import os
    from PIL import Image
    import re

    url1 = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
    file1 = urllib2.urlopen(url1)

    level7_name = 'level7.png'
    if os.path.exists(level7_name):
        print '%s is exits' %level7_name
        image1 = Image.open('level7.png')
        print "image information:"  ,image1.format, image1.size, image1.mode
        weight, high = image1.size
        print weight, high
        msg = ''.join([chr(image1.getpixel((i, 43))[0])for i in xrange(0, 609, 7)])
        print ''.join([chr(int(x)) for x in re.findall(r'\d{3}', msg)])

    else:
        with open(level7_name, 'wb') as f:
            f.write(file1.read())
    '''
    RGBA的值是（x,x,x,255）的形式，所以R、G、B三个中随便选一个就可以的，我看网上选的是R值，我选个R值吧！
    step的值为7，据说可以通过GIMP观察得到的。然后最后得到输出的结果为：smart guy, you made it. the next level
    is [105, 110, 116, 101, 103, 114, 105, 116, 121]
    '''


#level08
def level08():
    import bz2
    un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    print 'username: ' + bz2.decompress(un)
    print 'password: ' + bz2.decompress(pw)


#level09
def level09():
    import Image
    import ImageDraw
    #     from PIL import Image
    # from PIL import ImageDraw


    first= [
    146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170, 355, 169, 346, 167, 335, 170, 329, 170, 320, 170,
    310, 171, 301, 173, 290, 178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194, 307, 191, 312, 190, 316,
    190, 321, 192, 331, 193, 338, 196, 341, 197, 346, 199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197, 383, 196, 387, 192,
    389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402, 216, 401, 219, 397, 219, 393, 216, 390, 215, 385,
    215, 379, 213, 373, 213, 365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311, 215, 306, 216, 296, 218,
    290, 221, 283, 225, 282, 233, 284, 238, 287, 243, 290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273, 289, 278, 287,
    279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294, 291, 296, 295, 299, 300, 301, 304, 304, 320, 305,
    327, 306, 332, 307, 341, 306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302, 393, 324, 391, 333, 387,
    328, 375, 329, 367, 329, 353, 330, 341, 331, 328, 336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269, 344, 262, 346,
    259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295, 349, 298, 354, 293, 356, 286, 354, 279, 352, 268,
    352, 257, 351, 249, 350, 234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137, 339, 132, 330, 122, 327,
    120, 314, 116, 304, 117, 293, 118, 284, 118, 281, 122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134, 228, 136, 221, 137,
    214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159, 134, 157, 134, 160, 130, 170, 125, 176, 114, 176,
    102, 173, 103, 172, 108, 171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124, 115, 120, 115, 115, 117,
    113, 120, 109, 122, 102, 122, 100, 121, 95, 121, 89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130, 108, 132, 110,
    133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149, 77, 155, 81, 162, 90, 165, 97, 167, 99, 171, 109, 171, 107, 161,
    111, 156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259, 136, 266, 139, 276, 143, 290, 148, 310, 151,
    332, 155, 348, 156, 353, 153, 366, 149, 379, 147, 394, 146, 399
    ]
    second = [
    156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186, 150, 179, 155, 175, 157, 168, 157, 163, 157, 159,
    157, 158, 164, 159, 175, 159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146, 218, 143, 220, 132, 220,
    125, 217, 119, 209, 116, 196, 115, 185, 114, 172, 114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97, 167, 89, 164, 81, 162,
    77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126, 113, 129, 118, 117, 128, 114, 137, 115, 146, 114, 155, 115,
    158, 121, 157, 128, 156, 134, 157, 136, 156, 136
    ]

    im = Image.new('RGB', (700, 500))
    draw = ImageDraw.Draw(im)
    draw.line(first)
    draw.line(second)
    im.show()

def level10():
    a = '1'
    for i in xrange(30):
        pos = 0
        tmp = ''
        str_len = len(a)
        while pos < str_len:
            count = 1
            while pos + 1 < str_len and a[pos] == a[pos + 1]:
                count += 1
                pos += 1

            tmp += '%d%s' % (count, a[pos])
            pos += 1
        a = tmp
    print(len(a))

def level11():
    from PIL import Image
    img = Image.open('level11.jpg')

    w = img.size[0]
    h = img.size[1]

    odd = even = Image.new(img.mode, (w/2, h/2))

    for x in range(w):
        for y in range(h):
            pixel = img.getpixel((x, y))
            if x % 2 == 0 and y % 2 == 0:
                odd.putpixel((x/2, y/2), pixel)
            elif x % 2 == 1 and y % 2 == 0:
                even.putpixel(((x-1)/2, y/2), pixel)
            elif x % 2 == 0 and y % 2 == 1:
                even.putpixel((x/2, (y-1)/2), pixel)
            elif x % 2 == 1 and y % 2 == 1:
                odd.putpixel(((x-1)/2, (y-1)/2), pixel)

    odd.show()
    even.show()

#level12
def level12():
    with open('level12.gfx', 'rb') as f:
        data = f.read()
    # print data
    for i in range(5):
        file = open('evil_%d.jpg' % i, 'wb')
        file.write(data[i::5])
        file.close()
    f.close()

#level13
def level13():
    import xmlrpclib
    xmlrpc = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
    print xmlrpc.system.listMethods()
    print xmlrpc.system.methodHelp('phone')
    print xmlrpc.phone('Bert')

#level14
def level14():
    import re
    from PIL import Image
    im = Image.open(r'level14.png')
    result = Image.new(im.mode,(100,100))
    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    x,y = -1,0
    k = 0
    steps = 200
    while steps/2>0:
        for vector in direction:
            step = steps/2
            for i in range(step):
                x = x + vector[0]
                y = y + vector[1]
                pixel = im.getpixel((k,0))
                result.putpixel((x,y),pixel)
                k +=1
            steps -= 1
    result.show()

#level15
def level15():
    import datetime
    import calendar
    for  year in range(1006, 2006, 10):
        day = datetime.date(year, 1, 27)
        # print day
        if calendar.isleap(year)and day.weekday() == 1:
            print year

def level16():
    from PIL import Image
    import re
    im = Image.open(r'level16_mozart.gif')
    result = Image.new(im.mode,im.size)
    for y in range(im.size[1]):
        line = [im.getpixel((x,y)) for x in range(im.size[0])]
        temp = 0
        while line[temp]!=195:
            temp += 1
        new = line[temp:]+line[:temp]
        for x in range(len(new)):
            result.putpixel((x,y),new[x])
    result.show()

def level17():
    pass

#level18
def level18():
    import gzip
    data1 = gzip.open('level18_deltas.gz')
    data2 = open('level18_deltas2.gz')
    print data1 == data2



if __name__ == "__main__":
    # level0()
    # level1()
    # level2()
    # level3()
    # level4()
    level5()
