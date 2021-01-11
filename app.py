import logging
from threading import Event

logging.basicConfig(filename='sumpPump.log', level=logging.DEBUG)
stop_flag = Event()

try:
    logging.info('Application started!')
    #call app here
except KeyboardInterrupt:
    stop_flag.set()
    logging.error('Application interrupted by user')