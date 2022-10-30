from time import sleep
import button
import keyboard as kb
import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard

POKE_POSITION = 1732, 617
LIST_ATACKS = ['F1', 'F3', 'F6', 'F4', 'F2', 'F5']


def revive():
    my_position = pg.position()
    pg.moveTo(POKE_POSITION)
    pg.click(button="right")
    kb.press(button.key['TAB'])
    pg.click(button="right")
    pg.moveTo(my_position)


def atack(hotkey, delay=0.6):
    for item in hotkey:
        kb.press(button.key[item], delay)


def key_code(key):
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.end:
        revive()
    if key == keyboard.Key.page_down:
        atack(LIST_ATACKS)
    if key == keyboard.Key.delete:
        atack(LIST_ATACKS)
        revive()

with Listener(on_press=key_code) as listener:
    listener.join()