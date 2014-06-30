#urllib - module to manipulate data from web

import urllib as url

#getting raw html data from urlopen method
web_data = url.urlopen("https://docs.python.org/2/library/urllib.html")

#reading the raw html data from read method
print web_data.read()

#urlretrieve method can be used to download a specific web resources
web_content = url.urlretrieve("https://docs.python.org/2/library/urllib.html","urllib.html")
