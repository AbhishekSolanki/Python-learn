import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')


a = 0
b = 1
c = 0
logging.debug("a,b successfully initialized")
no = input("Enter range ")
if(no>100 or no<10):
    logging.warning('no. too big .....will take some time')
    logging.error("Technical error!")
    exit()
else:
    logging.info('no. in range, execution started')


while(c < no):
    a = b
    b = c
    print c
    c = a+b
logging.info("Finished")
