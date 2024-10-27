#import time
import pyttsx3
engine= pyttsx3.init()
print("Welcome sir....I'm a text to speech app")
engine.say("Welcome sir....I'm a text to speech app...")
#time.sleep(0.00005) 
#engine.say("please wait...so.")
#time.sleep(1) 
engine.say("What do you want to say...?")
engine.runAndWait()
while True:
  text = input("What do you want to say...? \n")
  if text == 'q':
    engine.say("THANKS TO USING ME")
    engine.runAndWait()
    break
  elif text == '001':
    engine.say("Teri behaan koo Naaman")
    engine.runAndWait()
  else:
    pass   
  engine.say(text)
  engine.runAndWait()