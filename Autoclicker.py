from pynput import keyboard
import mouse
import time
import threading

# press "end" to toggle autoclicker on and off
keybind = keyboard.Key.end
state = False

def click():
    while True:
        if state:
            print("autoclicker started")
            mouse.click("left")
        time.sleep(.01)
        
        
def toggle_event(key):
    if key == keybind:
        global state
        state = not state
        
        
click_thread = threading.Thread(target=click)
click_thread.start()

# Collect events until released
with keyboard.Listener(on_press=toggle_event) as listener:
    listener.join()