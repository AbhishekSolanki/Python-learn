# Calculate Execution time of program
import psutil
process = psutil.Process(os.getpid())
mem = process.get_memory_info()[0] / float(2 ** 20)
print mem
