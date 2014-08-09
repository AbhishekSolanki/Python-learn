# Author: AbhishekSolanki
import ConfigParser

def main():
    cp = ConfigParser.ConfigParser()
    cp.read("config.cfg")
    l = ["mentor","email"]

    for i in l:
        x = cp.get('SafeSquid',i)
        print i+" => "+x
if __name__=='__main__':
    main()
