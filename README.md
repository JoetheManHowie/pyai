# pyai

pyai is a simple module that provides a simple way to run and save content produced by openai. This module is based off the tutorial notebook in the [OpenAI repo here](https://github.com/JoetheManHowie/OpenAI). For a detailed walk through of the classes used in this module consult those notebook tutorials.


## Overview:

We have three main use cases for the (openai python api)[https://beta.openai.com/docs/api-reference/introduction]: text Completion, Image generation, and Code creation. See [notebook tutorials for details](https://github.com/JoetheManHowie/OpenAI).

Here we have three Classes that allow for easy use of the create methods for any of the three use cases.

1. TextCompletion
2. ImageGeneration

Each with similar api's, which allow you to: run prompts through the models, save the output, and display the generated result. 


## Setting up API key:

There are two ways to set up the api key for openai. In the Getting started tutorial notebooks we maually enter the key every time. That method becomes impractical after prolonged use. We recommend that users set these keys in their bash profiles (if you are on Linux/MacOS). I have not tested on windows yet on setting up the OPEN_API_KEY. If someone using the python API has done this feel free to comment or contribute and let me know :)

1. Open/Create `.profile` in your home directory (if you are on a M1(2020) or newer Mac, this is now called `.zprofile` because of zsh is used on these machine instead of bash).
2. Then include the following to lines: `OPENAI_API_KEY="your-key"`, and `export OPENAI_API_KEY`
3. Finally, restart the terminal or run the command `source .zprofile` to apply the change to the file


## TextCompletion:

