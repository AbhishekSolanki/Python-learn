import time
string = "Abhishek solanki"

st_time=time.time()
print string[::-1] #faster
print "exec time",time.time()-st_time

#print "".join(reversed(string)) #slower
