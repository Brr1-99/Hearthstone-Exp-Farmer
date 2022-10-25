import pyautogui
import subprocess
import time

screenWidth, screenHeight = pyautogui.size()

def open_hearthstone() -> None:
    subprocess.Popen(['C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe'])
    pyautogui.sleep(10)
    pyautogui.click(x=screenWidth/6, y=screenHeight*6/7)
    # The following lines will click the mercenaries button for you
    # pyautogui.sleep(20)
    # pyautogui.leftClick(x=screenWidth/2, y=screenHeight*4/9)

def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    return process_name in progs

go = True
stop = False 

while go:
    go = pyautogui.confirm(text='Hearthstone is gonna open soon. Want to proceed with it?', title='', buttons=[True, False])
    open_hearthstone()
    while process_exists('Hearthstone.exe'):
        time.sleep(5)
    stop = pyautogui.confirm(text='The timer will start now. Do you want to finish here?', title='', buttons=[True, False])
    if stop:
        break
    time.sleep(60*28)      
