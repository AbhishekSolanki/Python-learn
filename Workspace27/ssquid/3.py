# Author: AbhishekSolanki

def bytes_to_KB(inp_bytes):
    return str(inp_bytes/1024.00)+" KB"
def bytes_to_Kb(inp_bytes):
    return str(inp_bytes/1024.00*8) +" Kb"

def bytes_to_MB(inp_bytes):
    return str(inp_bytes/1024.00**2)+" MB"
def bytes_to_Mb(inp_bytes):
    return str(inp_bytes/(1024.00**2)*8) +" Mb"

def bytes_to_GB(inp_bytes):
    return str(inp_bytes/1024.00**3)+" GB"
def bytes_to_Gb(inp_bytes):
    return str(inp_bytes/(1024.00**3)*8) +" Gb"    

def main():
    inp_bytes = input("Enter bytes: ")
    print bytes_to_KB(inp_bytes)
    print bytes_to_Kb(inp_bytes)
    print bytes_to_MB(inp_bytes)
    print bytes_to_Mb(inp_bytes)
    print bytes_to_GB(inp_bytes)
    print bytes_to_Gb(inp_bytes)

if __name__=='__main__':
    main()
