import time
import pyautogui as pg

time.sleep(5)
pg.PAUSE = .2

for c in range(0, 10):
    pg.click(x=773, y=1032)
    pg.write('mariana gosta de comer!')
    pg.press('enter')