# Program to read last three line of the file


#function to find the no. of lines
def file_len(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


#Retrieving 
def lastThree(filename,n):
    Lines = file_len(filename)
    file_object = open(filename)
    data = file_object.readlines()
    for i in range(Lines-n,Lines):
        print data[i]


lastThree("file_to_read.txt",3)


