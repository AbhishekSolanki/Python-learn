user = raw_input("Enter your username ")
file_object = open("username1.txt","a")
file_object.write(user+"\n")
file_object.close()

file_object2 = open("username1.txt","r")
usernames = file_object2.read()
file_object2.close()
print "PERSISTENT DATA","\n"
print usernames
