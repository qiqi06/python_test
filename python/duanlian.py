#-*-coding: utf-8 -*-
#!/usr/bin/python

def duanlian():
	import time
	for i in range(30):
		time.sleep(0.9)
		print i





if __name__ == "__main__":
	print "模块主运行"
	duanlian()
else:
	print "模块被其他模块调用"
