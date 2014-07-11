# Program to read last three line of the file
import timing

#function to find the no. of lines
def file_len(filename):
    with file_object as f:
        for i, l in enumerate(f):
            pass
    return i + 1


#Retrieving 
def lastThree(filename,n):
    Lines = file_len(filename)
    file_object = open("file_to_read.txt")
    data = file_object.readlines()
    for i in range(Lines-n,Lines):
        print data[i]
    
    


file_object = open("file_to_read.txt")
lastThree("file_to_read.txt",3)

