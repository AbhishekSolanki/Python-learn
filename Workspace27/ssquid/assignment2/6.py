file_obj = open("6.txt","r")

names = {}

for each_name in file_obj:
    
    each_name = each_name.replace("\n",'')
    
    if each_name not in names:
        names[each_name]=1
    else:
        names[each_name]=names[each_name]+1

for i in names:
    print i,"-->",names[i]
