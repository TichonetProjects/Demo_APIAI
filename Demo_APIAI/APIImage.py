import openai
from openai import OpenAI

import io
import urllib.request
from PIL import Image
import matplotlib.pyplot as plt


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


#urlImage = createImage("A Polar bar dancing on the water with colorful fireworks around")
imgBase="Data/imgBase.png"
imgMask="Data/imgMask.png"
#urlImage = createImageEdit("A prompt describing the full image", imgBase, imgMask)
urlImage = createImageVariation(imgBase)

urllib.request.urlretrieve(urlImage, "TempImageName.png") 
img = Image.open("TempImageName.png") 
img.show()

