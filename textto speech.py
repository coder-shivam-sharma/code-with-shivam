from gtts import gTTS
language = "en"
text = "hello world, i am a student !"
speech = gTTS(text=text,lang= language, slow=False, tld="com.au")
speech.save("texttospeech12345.mp3")
#it needs internet connection