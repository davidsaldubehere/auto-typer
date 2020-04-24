import eel
import pyautogui as py
from pynput import mouse
import time

def getClickPos(x, y, button, pressed):
    print(x,y)
    eel.updateClick(x, y)
    return False

@eel.expose
def startListener():
    with mouse.Listener(on_click=getClickPos) as listener:
            listener.join()

@eel.expose
def start(data, delay):
    time.sleep(int(delay))
    breakData = data.split("$")
    print(breakData)
    for i in range(len(breakData)):
        if len(breakData[i])==1:
            try:
                time.sleep(int(breakData[i]))
            
            except Exception:
                pass
        
        elif len(breakData[i])!=1:
            py.typewrite(breakData[i], .1)

eel.init('web')
eel.start('index.html')