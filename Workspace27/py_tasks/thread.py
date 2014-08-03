import threading
import thread
import time

def timer(threadName,delay,repeat):
	print "Thread "+threadName+" Started ! "
	
	while repeat>0:
		time.sleep(delay)
		print threadName+":"+str(time.ctime(time.time()))
		repeat-=1
	print "Thread "+threadName+" Finished !"
	
def Main():
        pass
        t1 = thread.start_new_thread(timer,("one",2,5))
        t2 = thread.start_new_thread(timer,("two",2,5))
        t1.start()
        t2.start()

if __name__=='__main__':
        Main()
