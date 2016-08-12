#-*-coding:utf-8-*-
#/usr/bin/python

import multiprocessing
import time



#fork() only use in linux
def thread():
    import os 
    print "Process (%s)starting..." %os.getpid()
    pid = os.fork()
    if pid == 0:
        print " I am child process (%s) and my parent is %s" %(os.getpid(), os.getppid())
    else:
        print " I (%s) just created a child process(%s)." %(os.getpid(), pid)

def worker_1(interval):
    print "worker_1"
    time.sleep(interval)
    print "end worker_1"

def worker_2(interval):
    print "worker_2"
    time.sleep(interval)
    print "end worker_2"

def worker_3(interval):
    print "worker_3"
    time.sleep(interval)
    print "end worker_3"

def worker_4(interval):
    print "worker_4"
    time.sleep(interval)
    print "end worker_4"




if __name__ == "__main__":
    print "Main moudle is running !"
    
    #use fork()
    # thread()

    p1 =multiprocessing.Process(target = worker_1, args = (2,))
    p2 =multiprocessing.Process(target = worker_2, args = (3,))
    p3 =multiprocessing.Process(target = worker_3, args = (4,))
    p4 =multiprocessing.Process(target = worker_4, args = (4,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    print("The cpu number is :" + str(multiprocessing.cpu_count())+ "\n")
    for p in multiprocessing.active_children():
        print ("child p.name " + p.name +"\tp.id" +str(p.pid))
    print "End!!!"
else:
    print "moudle by running!"