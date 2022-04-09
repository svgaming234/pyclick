import pyautogui
import time

print('PyClick')
a = int(input('Enter the time between clicks(in seconds): '))
b = input('Enter the amount of clicks you want the program to click(leave blank to click until the program is closed): ')
c = 0

while True:
    time.sleep(a)
    pyautogui.click()
    print('Clicked.')
    # the part below is very messy,
    # but it was the only way i could make it click forever if left blank
    c = c + 1
    d = str(c)
    if d == b:
        break
