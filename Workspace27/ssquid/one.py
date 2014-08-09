# Author: AbhishekSolanki
import ConfigParser

cp = ConfigParser.ConfigParser()
cp.read("config.cfg")
l = ["mentor","email"]

for i in l:
    x = cp.get('SafeSquid',i)
    print i+" => "+x
