import time

import pyautogui


class Pause_cafe:

    def deplace_souris(self):
        while True:
            time.sleep(600)
            pyautogui.move(150, 150, 3, pyautogui.easeInElastic)
            pyautogui.move(-150, -150, 3, pyautogui.easeInElastic)
