import linecache

#using linecache Module
def lastThreeLines():
    lines = len(file_object.readlines())
    for i in range(lines,lines-3,-1):
        print linecache.getline("file_to_read.txt",i)
