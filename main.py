import pyautogui
import subprocess
import time
import datetime

stoptime = 28

screenWidth, screenHeight = pyautogui.size()

def open_hearthstone() -> None:
    subprocess.Popen(['C:/Program Files (x86)/Battle.net/Battle.net Launcher.exe'])
    pyautogui.sleep(10)
    pyautogui.click(x=screenWidth/6, y=screenHeight*6/7)
    # The following lines will click the mercenaries button for you
    # pyautogui.sleep(20)
    # pyautogui.leftClick(x=screenWidth/2, y=screenHeight*4/9)

def process_exists(process_name: str) -> bool:
    progs = str(subprocess.check_output('tasklist'))
    return process_name in progs

go = 'Yes'
stop = 'No' 

while True:
    go = pyautogui.confirm(text='Hearthstone is gonna open soon. Want to proceed with it?', title='', buttons=['Yes', 'No'])
    if go == 'No':
        break
    open_hearthstone()
    time.sleep(5)
    while process_exists('Hearthstone.exe'):
        time.sleep(5)
    stop = pyautogui.confirm(text='The timer will start now. Do you want to finish here?', title='', buttons=['Yes', 'No'])
    if stop == 'Yes':
        break
    now = datetime.datetime.now()
    end = now + datetime.timedelta(minutes=stoptime)
    pyautogui.alert(text=f'The timer will end at {end.strftime("%H:%M:%S")} in {stoptime} minutes', title='Timer has started', button='OK')
    print(f'The timer will end at {end.strftime("%H:%M:%S")}')
    time.sleep(stoptime*60)     
