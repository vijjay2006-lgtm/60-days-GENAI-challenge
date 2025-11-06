import pyautogui
import time
time.sleep(5)
x,y=pyautogui.position()
print("x:{x},y:{y}")


import pyautogui
import time

print("Move your mouse...")

while True:
    x, y = pyautogui.position()
    print(f"X: {x}, Y: {y}", end='\r')
    time.sleep(0.05)
    
    pyautogui.write("python mouse_control.py")
    pyautogui.press("vijay")


    pyautogui.write ("vijay balasubramanian")
    pyautogui.press("enter")


import pyautogui



