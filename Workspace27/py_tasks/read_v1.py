class test:
        
    def lastThree(self,filename,n):
        
        file_object = open(filename,"r")
        
        with file_object as f:
            no_of_lines = len(file_object.readlines())
            
            if(n>0 and n<=no_of_lines):
                file_object.seek(0)
                lines = file_object.readlines()
                file_object.close()
                for i in range(no_of_lines-n,no_of_lines):
                    print lines[i]
            else:
                file_object.close()
                print "Invalid line(s) selection"

testObj = test()
testObj.lastThree("file_to_read.txt",3)
