#!/usr/bin/env python3

## Two ways to call this program.

## EX: python3 TextCompletion.py <api key>[1] <text prompt>[2] 

## EX: python3 TextCompletion.py <api key>[1] <text prompt>[2] <temperature=1>[3] <max_token=2048>[4] <top_p=1>[5] <n=1>[6] <echo=True>[7] <frequency_penalty=1.2>[8] <presence_penalty=0.2>[9]

from time import time

import sys

from pathlib import Path
import openai as oai


class TextCompletion():
    def __init__(self, prompt, temperature=1, max_tokens=2048, top_p=1, n=1, echo=True, frequency_penalty=1.2, presence_penalty=1.2):
        # set class variables
        self.prompt = prompt
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.n = n
        self.echo = echo
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        # generate the text response
        self.response = self.generate_response()


    def __str__(self):
        return self.response.choices[0].text
        

    def generate_response(self):
        '''
        returns an oai.Completion.create data structure.
        use print(<your_object_name>) to see the text generated.
        use save_generated_text() to save the text generated.
        '''
        return oai.Completion.create(model="text-davinci-003",
                                     prompt=self.prompt,
                                     temperature=self.temperature, # def=1 (DO NOT use BOTH temperature and top_p)
                                     max_tokens=self.max_tokens, # def=16 (number of characters in response)
                                     top_p=self.top_p, # def=1 (DO NOT use BOTH temperature and top_p)
                                     n=self.n, # def=1 (number of completion)
                                     echo=self.echo, # def=False ()
                                     frequency_penalty=self.frequency_penalty, # [-2, 2] def=0 
                                     presence_penalty=self.presence_penalty) # [-2, 2] def=0

    
    def save_generated_text(self, text_generated="TextGenerated/", tolerance=250):
        '''
        prepare to save image to the ImagesGenerated folder.
        folder name is the prompt text with "-" in place of spaces
        each period makes a new chain in the directory path
        '''
        save_folder = self.prompt[:tolerance].lower().replace(" ", "-").replace(".-", "/").replace(".", "/") + "/"
        
        ## specific image name is the current time in micro seconds (ms)
        file_name = str(round(time()*1e6)) + ".txt"
        
        ## creates directory (folder) where instances of this prompt will be stored
        new_directory = Path(text_generated+save_folder)
        new_directory.mkdir(parents=True, exist_ok=True)
        
        ## save path for the generated image
        save_path_name = text_generated + save_folder + file_name
        with open(save_path_name, "w+") as writer:
            writer.write(self.response.choices[0].text)
            
        
####################################

def main():
    oai.api_key = sys.argv[1]
    prompt = sys.argv[2]
    tc = None
    t1 = time()
    if len(sys.argv) > 3:
        tc = TextCompletion(prompt, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9])
    else:
        tc = TextCompletion(prompt)
    print(tc)
    print("Time elapsed:", round(time()-t1, 3), "seconds")
    print()
    print("Would you like to save the output? [Y/n]")
    decide = input()
    if decide.lower().startswith("y"):
        tc.save_generated_text()
        
    
if __name__=="__main__":
    main()
    
