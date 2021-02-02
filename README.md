# AvaMotes

A small python program to display 9 different expressions for 2D only streamers using OBS. Currently only supports Windows but if you know Python commands, you can make it work on Mac or Linux.

### How to use

1. Download or clone the Avemotes.
2. To execute the program, go to Avemotes/dist/emotes.exe. If you know Python, use the command `python emotes.py` in the Avemotes root folder.
3. Once opened, click the `Output` button and select the folder that contains your emotes.
4. Click the hotkey# and select the image you want to bind to that key.
5. In OBS, create or use an existing image source and set its path to where/your/emotes/are/__current.png
6. Turn on your numpad and press a numpad number key. You should be able to see an image on your OBS scene.

**NOTE: Don't press the hotkeys too fast, wait for a second or two before pressing again**

### How it works

As I observed, as long as the file path from the source remains the same, you can essentially rename other files with the file path used in the source and OBS will render the renamed file on the go.

Avamotes takes advantages of that feature by creating an empty png file, `__current.png`, in a folder full of emote images. When the output file is set as the source image, as you press the hotkeys, the corresponding image that is bound to the hotkey is renamed to __current.png.

### Known Bugs

Currently, if you press the hotkeys too fast, the prior image would not show again, renaming the image as image_name.png.tmp. This is because the program takes some time to rename the file, about a second or two, and if you press the next hotkey too early, you will execute the renaming command way too soon.

### Resolving the Bug

If you get caught up with the bug, you need to go to your source folder and rename the image back to what it was before.

The best way to name the emotes is by using numbers (ex. 1.png, 2.png, 3.png, etc.). This is renamed faster than longer named ones.

### Open-source

Although I'm not new to programming, I AM new to Python itself. So if you know Python really well, it would be great if we could help each other out and make AvaMotes better. And if you want, feel free to make an even better version of this program.
