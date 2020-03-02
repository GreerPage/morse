# Morse Code for Raspberry Pi

This project is meant be run strictly on a Raspberry Pi. It assumes that you have an LED connected and properly wired to a breadboard using GPIO pin 18. 

![raspi](https://greerpage.com/static/images/raspidiagram.png)

## To run 
 - run morse.py, it takes one argument which is the message to be translated. 
 - EXAMPLE: ```python3 morse.py Hello World```

## Break Down of the Project
  - dotDash.py = defines the dot dash and space functions that are used to trigger or not trigger the led for the certain amount of time
  - morseKey.py = defines functions for all of the letters. For example it says that for the letter "e" do one dot. This is all brought together in the texttomorse function, which takes one argument which is the message to be translated.
  - morse.py = this takes a command line argument of the message you want to translate. It is the runner for the full project.

## What it does
 - When running morse.py it will translate the message you input into morse code and it will display it with the LED repeatedly until you exit the program (CTRL C).
 - It will also print out the translated message in the console every time the LED finishes.
 - EXAMPLE: ```python3 morse.py Hello World``` will output ```.... . .-.. .-.. --- / .-- --- .-. .-.. -.. / /```. If you put this into a morse to text converter [I suggest this one](https://morsecode.scphillips.com/translator.html) it will give you "HELLO WORLD".
