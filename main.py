import pyautogui

pyautogui.FAILSAFE = False
from pynput import keyboard
import time
import random
from datetime import datetime


def on_press(key):
    if key == keyboard.Key.esc:
        global running
        running = False


running = True
if __name__ == '__main__':
    print('press esc touch to escape')
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while running:
        time.sleep(0.01)
        x, y = random.randint(0, 10) - 5, random.randint(0, 10) - 5
        pyautogui.moveRel(x, y)
        if random.random() > 0.9:
            pyautogui.press('shift')
