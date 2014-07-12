# Calculate Execution time of program
import time


file_to_execute = raw_input("Enter file name:")
note = raw_input("Enter test note: ")
start_time = time.time()
exec('import %s' % file_to_execute)
final_time=time.time() - start_time
file_object = open(file_to_execute+"_execlog.txt","a")
file_object.write(str(final_time*1000)+" ms ## "+note+"\n")
file_object.close() 
print final_time

