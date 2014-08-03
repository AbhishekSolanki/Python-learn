#pg 162
import thread
from time import ctime,sleep

def loop0():
	print "Start loop 0 at",ctime()
	sleep(4)
	print "loop0 done at", ctime()

def loop1():
	print "start loop1 at",ctime()
	sleep(2)
	print "loop1 done at",ctime()

def main():
	print "starting at", ctime()
	loop0()
	loop1()
	print "all done at",ctime()

main() 
