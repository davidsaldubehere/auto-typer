import eel
import pyautogui
from pynput import mouse

def getClickPos(x, y, button, pressed):
    print(x,y)
    eel.updateClick(x, y)
@eel.expose
def startListener():
    with mouse.Listener(
        on_click=getClickPos) as listener:
            listener.join()


eel.init('web')
eel.start('index.html')