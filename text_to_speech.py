# MatiusXIII
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pyfiglet import Figlet
import gtts
import time
import sys
from pygame import mixer
import threading

text = ''
prev_text = ''

def getText():
    while True:
        global text
        text = input()
        if text == 'exit':
            sys.exit(0)

def playText():
    global text
    global prev_text
    while True:
        if text != prev_text and text != 'exit':
            sound = gtts.gTTS(text, lang='ru')
            sound.save('Sound.mp3')
            # Enter in line below in 'devicename' your VAC
            mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
            mixer.music.load('Sound.mp3')
            mixer.music.play()
            while mixer.music.get_busy() == True:
                time.sleep(1)
            prev_text = text
            mixer.quit()
        elif text == 'exit':
            sys.exit(0)

def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText(text='XIII'))
    get = threading.Thread(target=getText)
    get.start()
    play = threading.Thread(target=playText)
    play.start()

if __name__ == '__main__':
    main()
