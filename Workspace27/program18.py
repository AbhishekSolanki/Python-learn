#XML Parsing - Parsing raw data

import urllib as url
import xml.etree.ElementTree as et

#creatinng url object
web_data = url.urlopen("http://www.w3schools.com/xml/cd_catalog.xml")
str_data = web_data.read()

#Creating xml data object (xml element tree object)
xml_data = et.fromstring(str_data)

#finding element
cd_list = xml_data.findall("CD")

#List to hold CD Prices
cd_prices = []

#function to add the price of all CDs
def addPrices(A):
    result = 0
    for i in A:
        result= result+i
    return result

#finding the attributes from each xml element
for i in cd_list:
    print i.find("TITLE").text #finding the attribute value from element
    cd_prices.append(float(i.find("PRICE").text))

print addPrices(cd_prices)
