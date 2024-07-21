import openai
from openai import OpenAI

import io
import urllib.request
from PIL import Image
import matplotlib.pyplot as plt

client = OpenAI()

def createText():
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
      ]
    )
    return completion.choices[0].message.content

def createImage(text):
    prefixPrompt = "I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS: "
    response = client.images.generate(
      model="dall-e-3",
      prompt=text,
      size="1024x1024",
      quality="standard",
      n=1,
    )
    return response.data[0].url

"""
DALL·E 2 only!
Edit or extend an image by uploading an image and mask indicating 
which areas should be replaced. 
The transparent areas of the mask indicate where the image should be 
edited, and the prompt should describe the full new image, 
not just the erased area. 
This endpoint can enable experiences like DALL·E image editing in ChatGPT Plus.
The uploaded image and mask must both be square PNG images less than 4MB in size, 
and also must have the same dimensions as each other. 
The non-transparent areas of the mask are not used when generating the output, 
so they don’t necessarily need to match the original image.
"""

def createImageEdit(text, imgBase, imgMask):
    response = client.images.edit(
      model="dall-e-2",
      image=open(imgBase, "rb"),
      mask=open(imgMask, "rb"),
      prompt=text,
      n=1,
      size="1024x1024"
    )
    return response.data[0].url


"""
DALL·E 2 only!
"""
def createImageVariation(imgToVarient):
    response = client.images.create_variation(
      model="dall-e-2",
      image=open(imgToVarient, "rb"),
      n=1,
      size="1024x1024"
    )
    return response.data[0].url


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


#print(createText())
#urlImage = createImage("A Polar bar dancing on the water with colorful fireworks around")
imgBase="C:/Users/Abhishek/Downloads/TempImageName.png"
imgMask="C:/Users/Abhishek/Downloads/TempImageName.png"
urlImage = createImageEdit("A prompt describing the full image", imgBase, imgMask)
utlImage = createImageVariation(imgBase)

urllib.request.urlretrieve(urlImage, "TempImageName.png") 
img = Image.open("TempImageName.png") 
img.show()





















































































