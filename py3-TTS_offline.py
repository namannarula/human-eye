import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice','english+f3') 
engine.say("The Times of India is an Indian English language daily newspaper owned by The Times Group. It is the fourth-largest newspaper in India by circulation and largest selling English-language daily in the world according to Audit Bureau of Circulations")
engine.runAndWait()


