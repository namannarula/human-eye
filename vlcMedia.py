import time
import vlc

player = vlc.MediaPlayer("abs.mp3")

player.play()

time.sleep(5)
