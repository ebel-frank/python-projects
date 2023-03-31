import os

def openFile():
    try:
        os.startfile("Python Tutorial.mp4")
    except Exception as e:
        print(str(e))

def closeFile():
    try:
        os.system("TASKKILL /F /IM notepad.exe")
    except Exception as e:
        print(str(e))
