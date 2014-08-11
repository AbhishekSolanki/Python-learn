file_obj = open("file.txt","r")
word_list=file_obj.read().lower().split()
print sorted(word_list)

