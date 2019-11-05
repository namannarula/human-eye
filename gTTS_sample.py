from gtts import gTTS
import vlc
import time
tts = gTTS(text="The Times of India is an Indian English language daily newspaper owned by The Times Group. It is the fourth-largest newspaper in India by circulation and largest selling English-language daily in the world according to Audit Bureau of Circulations", lang='en')
tts.save("abs.mp3")
player = vlc.MediaPlayer("/home/pi/Desktop/abs.mp3")
player.play()

time.sleep(20)


