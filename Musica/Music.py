from pygame import mixer
mixer.init()

mixer.music.load('Hoist.mp3')
mixer.music.play()
input('Está escutando')
mixer.event.wait()
