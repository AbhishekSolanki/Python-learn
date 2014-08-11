file_object = open("5.txt","r")
search_string="string occurence in file"
search_string=search_string.replace(" ",'')
count_occurence = 0

def find_all(original_string, search_string):
    start_pt=0
    count = 0
    len_search_string = len(search_string)
    while True:
        start = original_string.find(search_string, start_pt)
        if start == -1:
            return count
        else:
            count+=1
            start_pt = start+len_search_string

for i in file_object:
    temp_line = i.replace(" ",'')
    if search_string in temp_line:
        count_occurence+=find_all(temp_line,search_string)

print count_occurence
        
