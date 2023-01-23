#!/usr/bin/env python3AA



## imports
import os
from pathlib import Path
import openai as oai

## for reading urls and displaying images
from PIL import Image
import requests
from io import BytesIO

from time import time

class ImageGeneration():
    '''
    
    '''
    def __init__(self, prompt, n=1, size="512x512", response_format="url"):
        self.prompt = prompt
        self.n = n
        self.size = size
        self.response_format = response_format
        self.image = None
        self.generate_image()
        

    def set_prompt(self, prompt):
        '''
        Sets the prompt variable
        '''
        self.prompt = prompt


    def set_n(self, n=1):
        '''
        Number of imgaes the ai generates. It only returns the 'best' one out of the bunch.
        Range is [1,10], but watch out for RateLimitError, which can occur fast when n is large.
        Recommend using n=1 (which is the default value)'''
        self.n = n


    def set_size(self, size="512x512"):
        """
        Sets the size variable (reset to default when no value passed)
        Only three sizes '256x256', '512x512', '1024x1024'
        """
        self.size = size


    def set_response_format(self, response_format="url"):
        '''
        
        '''
        self.response_format = response_format


    def generate_image(self):
        '''
        
        '''
        image_resp = oai.Image.create(prompt=self.prompt, n=self.n, size=self.size)
        resp = requests.get(image_resp['data'][0]['url'])
        self.image = Image.open(BytesIO(resp.content))
        self.show_image()
        

    def show_image(self):
        '''
        
        '''
        self.image.show(self.image)


    def save_image(self, images_generated="GeneratedImages/", tolerence=250):
        ## prepare to save image to the ImagesGenerated folder.
        # to pruning the prompt name for saving
        ## folder name is the prompt text with "-" in place of spaces
        ## each period makes a new chain in the directory path
        save_folder = self.prompt[:tolerence].lower().replace(" ", "-").replace(".-", "/").replace(".", "/") + "/"
        
        ## specific image name is the current time in micro seconds (ms)
        file_name = str(round(time()*1e6)) + ".png"
        
        ## creates directory (folder) where instances of this prompt will be stored
        new_directory = Path(images_generated+save_folder)
        new_directory.mkdir(parents=True, exist_ok=True)
        
        ## save path for the generated image
        save_path_name = images_generated + save_folder + file_name
        self.image.save(fp=save_path_name)
        

def main():
    oai.api_key = sys.argv[1]
    prompt = sys.argv[2]
    tc = None
    t1 = time()
    if len(sys.argv) > 3:
        tc = ImageGeneration(prompt, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9])
    else:
        tc = ImageGeneration(prompt)
    print(tc)
    print("Time elapsed:", round(time()-t1, 3), "seconds")
    print()
    print("Would you like to save the output? [Y/n]")
    decide = input()
    if decide.lower().startswith("y"):
        tc.save_generated_text()


if __name__=="__main__":
    main()
