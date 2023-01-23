#!/usr/bin/env python3

## Two ways to call this program.

## EX: python3 TextCompletion.py <api key>[1] <text prompt>[2] 

## EX: python3 TextCompletion.py <api key>[1] <text prompt>[2] <temperature=1>[3] <max_token=2048>[4] <top_p=1>[5] <n=1>[6] <echo=True>[7] <frequency_penalty=1.2>[8] <presence_penalty=0.2>[9]

from time import time

import sys

from pathlib import Path
import openai as oai


class TextCompletion():
    '''
    TextCompletion is a simple wrapper class for openai's text completion tool. See: https://github.com/JoetheManHowie/pyai 
    For an intro to the python api please see the github page: https://github.com/JoetheManHowie/OpenAI
    This class allows for easy generation of AI produced text, with methods to save the text produced.
    Purpose of this class is to build pipelines which connect the output of text completion to the input of others.
    '''
    def __init__(self, prompt, model="text-davinci-003", temperature=0.9, max_tokens=2048, top_p=1, n=1, echo=True, frequency_penalty=1.2, presence_penalty=0.2):
        '''
        Initializes the class variables and generates response to the given prompt.
        The class variable can be changed or reset to default by calling the 'set_' methods.
        '''
        # set class variables
        self.prompt = prompt
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.n = n
        self.echo = echo
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        # generate the text response
        self.response = None
        self.generate_response()


    def __str__(self):
        '''
        returns the text response of the AI
        '''
        return self.response.choices[0].text


    def __repr__(self):
        '''
        returns the text response of the AI
        '''
        return self.response.choices[0].text
    
    
    def set_prompt(self, prompt):
        '''
        Sets the prompt variable
        '''
        self.prompt = prompt

        
    def set_model(self, model):
        '''
        Sets the model, do not recommend changing lightly
        '''
        self.model = model


    def set_temperature(self, temperature=1):
        '''
        Sets the temperature variable (reset to default when no value passed)
        Range is [0,1] (See OpenAI docs for details).
        NB: only temperature or top_p can be set to a value aside from default (See OpenAI docs for details)
        '''
        self.temperature = temperature
        self.top_p = 1


    def set_top_p(self, top_p):
        '''
        Sets the top_p variable (reset to default when no value passed)
        Range is [0,1] (See OpenAI docs for details).
        NB: only top_p or temperature can be set to a value aside from default (See OpenAI docs for details)
        '''
        self.temperature = 1
        self.top_p = top_p

    
    def set_n(self, n=1):
        '''
        Sets the n variable (reset to default when no value passed).
        Range is n >= 1, we recommend n=1 (default) because of rendering limits
        '''
        self.n = n


    def set_echo(self, echo=True):
        '''
        Sets the echo variable (reset to default when no value passed)
        Range is [True, False]
        '''
        self.echo = bool(echo)


    def set_frequency_penalty(self, frequency_penalty=1.2):
        '''
        Sets the frequency_penalty variable (reset to default when no value passed)
        Range is [-2,2] (See OpenAI docs for details).
        '''
        self.frequency_penalty = frequency_penalty


    def set_presence_penalty(self, presence_penalty):
        '''
        Sets the presence_penalty variable (reset to default when no value passed)
        Range is [-2,2] (See OpenAI docs for details).
        '''
        self.presence_penalty = presence_penalty
        

    def generate_response(self):
        '''
        returns an oai.Completion.create data structure.
        use print(<your_object_name>) to see the text generated.
        use save_generated_text() to save the text generated.
        '''
        self.response = oai.Completion.create(model=self.model,
                                              prompt=self.prompt,
                                              temperature=self.temperature, # def=1 (DO NOT use BOTH temperature and top_p)
                                              max_tokens=self.max_tokens, # def=16 (number of characters in response)
                                              top_p=self.top_p, # def=1 (DO NOT use BOTH temperature and top_p)
                                              n=self.n, # def=1 (number of completion)
                                              echo=self.echo, # def=False ()
                                              frequency_penalty=self.frequency_penalty, # [-2, 2] def=0 
                                              presence_penalty=self.presence_penalty) # [-2, 2] def=0
        
        
    def save_generated_text(self, text_generated="GeneratedText/", tolerance=250):
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
    
