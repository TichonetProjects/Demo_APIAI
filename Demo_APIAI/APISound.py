
#!sudo apt install espeak
#!pip3 install pyaudio
#!sudo apt install python3-pyaudio
#!pip3 install pyttsx3




import os
import pyttsx3 as p
#speak() converts text to speech
p.speak("I want to speak!")
#loops until user specify to quit
while True:
  p.speak("what can I do for you ?  ")
  userinput = input()
  #opens Microsoft Edge
  if ("run" in userinput and ("Microsoft Edge" in userinput)) or ("execute" in userinput and ("Microsoft Edge" in userinput)) or ("open" in userinput and ("Microsoft Edge" in userinput)) or ("launch" in userinput and ("Microsoft Edge" in userinput)) :
    p.speak("Microsoft Edge will be launched soon")
    os.system("msedge")
  #opens Powerpoint
  elif ("run" in userinput and ("Powerpoint" in userinput)) or ("execute" in userinput and ("Powerpoint" in userinput)) or ("open" in userinput and ("Powerpoint" in userinput)) or ("launch" in userinput and ("Powerpoint" in userinput)) :
    p.speak("Paint will be opened soon")
    os.system("POWERPNT")
  #It stops the execution
  elif ("exit" in userinput) or ("quit" in userinput):
    p.speak("Thanks for opting me . Share your smiles")
    break
	#If user inputs anything wrong, it shows don't support
  else:
    	print("don't support")
       
def training_data(data):
    return """Please predict text as positive or negative.
    text: You are a bad man.
    sentiment: negative
    text: You are good man.
    sentiment: positive
    text: {}
    sentiment:""".format(data.capitalize())

def Sentiment_APP(text):
    res=openai.Completion.create(
    model='text-davinci-003',
    prompt=training_data(text),
    max_tokens=20)
    return res.choices[0].text














my_api_key = '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'
