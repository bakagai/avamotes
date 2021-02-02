import os.path as path
import os
import tkinter as tk
import tkinter.filedialog as fileDialog
import json
import keyboard
import time

settingsFile = "__settings.json"
currentFile = "/__current.png"
settings = {}
root = tk.Tk()

root.winfo_toplevel().title("Avamotes")

canvas = tk.Canvas(root, width = 300, height = 330)
canvas.pack()


def fileExists(file):
    return path.exists(file)

def loadSettings():
    global settings
    with open(settingsFile, 'r') as reader:
        settings = json.loads(reader.read())

def updateSettings(data):
    with open(settingsFile, 'w') as outfile:
        json.dump(data, outfile)

def setOutputPath():
    global settings
    filePath = fileDialog.askdirectory();
    dirTextLabel.set(filePath)

    if not fileExists((filePath + currentFile)) and len(filePath) > 0:
        createEmptyFile(filePath + currentFile)

    if not settings['output'] == (filePath + currentFile) or settings['current'] == (filePath + currentFile):
        settings['output'] = filePath + currentFile
        updateSettings(settings)

def setImagePath(hotkey, stringVar):
    global settings
    filePath = fileDialog.askopenfilename();

    if len(filePath) > 0:
        stringVar.set(filePath)
        settings[hotkey] = filePath
        updateSettings(settings)

def changeEmote(hotkey):
    global settings

    if not settings["current"] == settings[hotkey]:

        if fileExists(settings["current"]):
            os.rename(settings["current"], settings["current"] + ".tmp")
            os.rename(settings["output"], settings["current"])
            os.rename(settings["current"] + ".tmp", settings["output"])

        os.rename(settings[hotkey], settings[hotkey] + ".tmp")
        os.rename(settings["output"], settings[hotkey])
        os.rename(settings[hotkey] + ".tmp", settings["output"])

        settings["current"] = settings[hotkey]
        updateSettings(settings)

def createEmptyFile(filename, text=""):
    file = open(filename, "w+")
    file.write(text)
    file.close()

def setEntryTexts():
    dirTextLabel.set(settings["output"])
    img1TextLabel.set(settings["1"])
    img2TextLabel.set(settings["2"])
    img3TextLabel.set(settings["3"])
    img4TextLabel.set(settings["4"])
    img5TextLabel.set(settings["5"])
    img6TextLabel.set(settings["6"])
    img7TextLabel.set(settings["7"])
    img8TextLabel.set(settings["8"])
    img9TextLabel.set(settings["9"])

def init():
    if not fileExists(settingsFile):
        defaultSettings = {
            "output": "",
            "current": "",
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": "",
            "9": ""
        }
        updateSettings(defaultSettings)

    loadSettings()
    setEntryTexts()
    root.mainloop()


dirTextLabel = tk.StringVar()
dirTextLabel.set("Hello World!")
dirLabel = tk.Entry(root, textvariable=dirTextLabel)
canvas.create_window(180, 20, window=dirLabel)

dirButton = tk.Button(text='Output',command=setOutputPath, bg='brown',fg='white')
canvas.create_window(60, 20, window=dirButton)

# Image 1
img1TextLabel = tk.StringVar()
img1TextLabel.set("Hello World!")
img1Label = tk.Entry(root, textvariable=img1TextLabel)
canvas.create_window(180, 50, window=img1Label)

img1Button = tk.Button(text='Hotkey 1',command=lambda:setImagePath("1", img1TextLabel), bg='brown',fg='white')
canvas.create_window(60, 50, window=img1Button)

# Image 2
img2TextLabel = tk.StringVar()
img2TextLabel.set("Hello World!")
img2Label = tk.Entry(root, textvariable=img2TextLabel)
canvas.create_window(180, 80, window=img2Label)

img2Button = tk.Button(text='Hotkey 2',command=lambda:setImagePath("2", img2TextLabel), bg='brown',fg='white')
canvas.create_window(60, 80, window=img2Button)

# Image 3
img3TextLabel = tk.StringVar()
img3TextLabel.set("Hello World!")
img3Label = tk.Entry(root, textvariable=img3TextLabel)
canvas.create_window(180, 110, window=img3Label)

img3Button = tk.Button(text='Hotkey 3',command=lambda:setImagePath("3", img3TextLabel), bg='brown',fg='white')
canvas.create_window(60, 110, window=img3Button)

# Image 4
img4TextLabel = tk.StringVar()
img4TextLabel.set("Hello World!")
img4Label = tk.Entry(root, textvariable=img4TextLabel)
canvas.create_window(180, 140, window=img4Label)

img4Button = tk.Button(text='Hotkey 4',command=lambda:setImagePath("4", img4TextLabel), bg='brown',fg='white')
canvas.create_window(60, 140, window=img4Button)

# Image 5
img5TextLabel = tk.StringVar()
img5TextLabel.set("Hello World!")
img5Label = tk.Entry(root, textvariable=img5TextLabel)
canvas.create_window(180, 170, window=img5Label)

img5Button = tk.Button(text='Hotkey 5',command=lambda:setImagePath("5", img5TextLabel), bg='brown',fg='white')
canvas.create_window(60, 170, window=img5Button)

# Image 6
img6TextLabel = tk.StringVar()
img6TextLabel.set("Hello World!")
img6Label = tk.Entry(root, textvariable=img6TextLabel)
canvas.create_window(180, 200, window=img6Label)

img6Button = tk.Button(text='Hotkey 6',command=lambda:setImagePath("6", img6TextLabel), bg='brown',fg='white')
canvas.create_window(60, 200, window=img6Button)

# Image 7
img7TextLabel = tk.StringVar()
img7TextLabel.set("Hello World!")
img7Label = tk.Entry(root, textvariable=img7TextLabel)
canvas.create_window(180, 230, window=img7Label)

img7Button = tk.Button(text='Hotkey 7',command=lambda:setImagePath("7", img7TextLabel), bg='brown',fg='white')
canvas.create_window(60, 230, window=img7Button)

# Image 8
img8TextLabel = tk.StringVar()
img8TextLabel.set("Hello World!")
img8Label = tk.Entry(root, textvariable=img8TextLabel)
canvas.create_window(180, 260, window=img8Label)

img8Button = tk.Button(text='Hotkey 8',command=lambda:setImagePath("8", img8TextLabel), bg='brown',fg='white')
canvas.create_window(60, 260, window=img8Button)

# Image 9
img9TextLabel = tk.StringVar()
img9TextLabel.set("Hello World!")
img9Label = tk.Entry(root, textvariable=img9TextLabel)
canvas.create_window(180, 290, window=img9Label)

img9Button = tk.Button(text='Hotkey 9',command=lambda:setImagePath("9", img9TextLabel), bg='brown',fg='white')
canvas.create_window(60, 290, window=img9Button)

def keyHandler(event):
    print(event.scan_code)
    if event.scan_code == 79:
        changeEmote("1")
        time.sleep(1)
    if event.scan_code == 80:
        changeEmote("2")
    if event.scan_code == 81:
        changeEmote("3")
    if event.scan_code == 75:
        changeEmote("4")
    if event.scan_code == 76:
        changeEmote("5")
    if event.scan_code == 77:
        changeEmote("6")
    if event.scan_code == 71:
        changeEmote("7")
    if event.scan_code == 72:
        changeEmote("8")
    if event.scan_code == 73:
        changeEmote("9")

keyboard.on_press(keyHandler, suppress=False)

init()
