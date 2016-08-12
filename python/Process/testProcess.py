#-*-coding:utf-8-*-
from multiprocessing import Process
from multiprocessing import Pool
import os, random, time


def run_proc(name):
    print " child process %s(%s) is running  " %(name, os.getpid())


def main_proc():
    print " Parent process %s is running" %os.getpid()
    p = Process(target = run_proc, args=('test',))
    print " Process will start"
    p.start()
    p.join()
    print "Process end"

def long_time_task(name):
    print " process %s(%s)is running " %(name, os.getpid())
    start = time.time()
    time.sleep = (random.random() * 100)
    end = time.time()
    print " Task %s run %0.2f seconds" %(name, (end - start))

def main_proc2():
    print " Parent process(%s) is running" %os.getpid()
    p = Pool()
    for i in range(5):
	#not same as Process
        p.apply_async(long_time_task, args=(i,))
    print "Waiting for all process done\n"
    p.close()
    p.join()
    print "All process done"



if __name__ == "__main__":
    print "main module is running "
    main_proc2()




else:
    print "module is by running "
