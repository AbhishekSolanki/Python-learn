import logging

log = logging.getLogger('71')
log.setLevel(logging.WARN)
log.addHandler(logging.StreamHandler())

def myfun():
    log.debug("Everthing prepared and fine")
    log.info("Flight ready to take off")
    log.warn("Signalling low fuel")
    log.error("Technical error!")
    log.critical("Preparing to land")   
