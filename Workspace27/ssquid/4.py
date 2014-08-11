import re

log_instance = open("extended.log","r")
regex=re.compile('\"(?P<id>([^-]*))[^ ]* (?P<elapsed_time>([\d]*)) (?P<client_ip>([.\d]*)) \"(?P<username>[^ ]*)\" \"(?P<connection_id>([^ ]*))\" \[(?P<datetime>([^ ]*))] \"(?P<method_url>([^"]*))\" (?P<httpstatus>([\d]*)) (?P<byte_transferred>([\d]*)) \"(?P<referrer_url>([^"]*))\" \"(?P<user_agent>([^"]*))\" (?P<mime>([^ ]*)) \"(?P<filter_name>([^"]*))\" \"(?P<filter_profile>([^"]*))\" \"(?P<interface>([^"]*))')

ids=[]
elapsed_time=[]
client_ip=[]
username=[]
connection_id=[]
datetime=[]
method_url=[]
httpstatus=[]
byte_transferred=[]
referrer_url=[]
user_agent=[]
mime=[]
filter_name=[]
filter_profile=[]
interface=[]

for line in log_instance:
    m = regex.search(line)
    ids.append(m.group("id"))
    elapsed_time.append(m.group("elapsed_time"))
    client_ip.append(m.group("client_ip"))
    client_ip.append(m.group("client_ip"))
    username.append(m.group("username"))
    connection_id.append(m.group("connection_id"))
    datetime.append(m.group("datetime"))
    method_url.append(m.group("method_url"))
    httpstatus.append(m.group("httpstatus"))
    byte_transferred.append(m.group("byte_transferred"))
    referrer_url.append(m.group("referrer_url"))
    user_agent.append(m.group("user_agent"))
    mime.append(m.group("mime"))
    filter_name.append(m.group("filter_name"))
    filter_profile.append(m.group("filter_profile"))
    interface.append(m.group("interface"))

print ids
print elapsed_time
print client_ip
print username
print connection_id
print datetime
print method_url
print httpstatus
print byte_transferred
print referrer_url
print user_agent
print mime
print filter_name
print filter_profile
print interface

    
    
   
    
