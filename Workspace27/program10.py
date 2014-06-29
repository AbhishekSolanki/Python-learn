#Dictionary exmaple
        
item_catalog = {"Blank CD's":7.99,"USB Drives":12.50,"Keyboards":18.00}
for x in item_catalog:
    print x

# Function to check whether the key in dictionary exist or not
def exists_in(DICT,NAME):
    result = False
    for x in DICT: 
        if x == NAME:
            result = True
    return result


# main loop
exit_var = False
while(exit_var == False):
    in_var = raw_input("Enter a product to look up its price ( or press x to quit )")
    if(exists_in(item_catalog,in_var)):
        print "Price is:",item_catalog[in_var]
    if(exists_in(item_catalog,in_var) == False and in_var != "x"):
        print "That item does not exist"
    if(in_var == "x"):
        exit_var = True

        
