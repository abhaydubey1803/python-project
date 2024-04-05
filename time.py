from time import  strftime
import pyttsx3
s = int(strftime("%H"))
engine = pyttsx3.init()
if s>=1 and s<=10:
    engine.say("good mornig abhay")
elif s>=11 and s<=17:
    engine.say("good afternoon abhay") 
else:
   engine.say("good night abhay")
engine.runAndWait() 