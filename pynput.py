from pynput.keyboard import Key,Controller
keyboard = Controller()
import time
def say(word):
    time.sleep(5)
    keyboard.type(word)
    keyboard.press("Key.enter")
    keyboard.release("Key.enter")
say("Hello")
