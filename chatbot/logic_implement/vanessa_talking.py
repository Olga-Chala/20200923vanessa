import os
import gtts
from gtts import gTTS
import tempfile
import pygame


def say(phrase):
    try:
        tts = gTTS(text=phrase, lang = "ru")
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=True) as f:
            tmpfile = f.name
        
        tts.save(tmpfile)
        play_mp3(tmpfile)
        print(tmpfile)
#         os.unlink(tmpfile)
#         os.remove(tmpfile)
        return tmpfile
    except PermissionError:
        pass
    
def play_mp3(filename):
    print('here')
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    print('finish')


