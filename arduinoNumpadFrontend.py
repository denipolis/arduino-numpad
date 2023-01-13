import serial
import pyautogui

# CONFIGURATION

COMPORT = "COM3"
BAUDRATE = 9600
TIMEOUT = 1

# CONFIGURATION

ser = serial.Serial(COMPORT, BAUDRATE, timeout=TIMEOUT)

while True:
	readed = ser.readline().decode("utf-8").split("\n")[0]

	if readed != "":
		print(readed)
	if readed == "pressed.1":
		pyautogui.press("num1")
	if readed == "pressed.2":
		pyautogui.press("num2")
	if readed == "pressed.3":
		pyautogui.press("num3")
	if readed == "pressed.4":
		pyautogui.press("num4")
	if readed == "pressed.5":
		pyautogui.press("num5")
	if readed == "pressed.6":
		pyautogui.press("num6")
	if readed == "pressed.7":
		pyautogui.press("num7")
	if readed == "pressed.8":
		pyautogui.press("num8")
	if readed == "pressed.9":
		pyautogui.press("num9")
	if readed == "pressed.0":
		pyautogui.press("num0")