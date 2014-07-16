import re

line = "Hi! this is Abhishek"

sobj = re.search(r'^(A.*)$',line)

print sobj.group(1)
