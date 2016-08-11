#coding: utf-8

#一年有多少天，这是个大问题，很值得思考。现在给你一个年份year(year为四位数字的字符串，如"2008","0012"),
#你输出这一年的天数。如year="2013", 则输出365。
def test02():
    import datetime
    year = 2007
    print datetime.datetime(int(year), 12, 31).timetuple()[7]




#给你一个时间t（t是一个字典，共有六个字符串key(year,month,day,hour,minute,second),值为每个值为数字组成的字符串，
#如t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
#请将其按照以下格式输出， 格式:XXXX-XX-XX XX:XX:XX。如上例应该输出： 2013-09-30 16:45:02。
def test03():
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