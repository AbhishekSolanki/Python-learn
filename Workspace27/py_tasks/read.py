# Program to read last three line of the file


#function to find the no. of lines
def file_len():
    with open("file_to_read.txt","r") as f:
        for i, l in enumerate(f):
            pass
    return i + 1


file_object = open("file_to_read.txt","r")

#Retrieving 
def lastThree(n):
    Lines = file_len()
    data = file_object.readlines()
    for i in range(Lines-n,Lines):
        print data[i]


lastThree(3)


