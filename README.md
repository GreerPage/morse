# Morse Code for Raspberry Pi

This project is meant be run strictly on a Raspberry Pi. It assumes that you have an LED connected and properly wired to a breadboard using GPIO pin 18 ([see this link](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins#:~:targetText=Use%20one%20of%20the%20jumper,the%20breadboard%2C%20as%20shown%20above.)).

To run: run morseexe.py, it takes one argument which is the message to be translated. EXAMPLE: python3 morseexe.py Hello World

### Breakdown of the project:
  - morse.py = defines the dot dash and space functions that are used to trigger or not trigger the led for the certain amount of time
  - morseKey1.py = defines functions for all of the letters. For example it says that for the letter "e" do one dot. This is all brought together in the texttomorse function, which takes one argument which is the message to be translated.
  - morseexe.py = this takes a command line argument of the message you want to translate. It is the runner for the full project.

### What it does:
    - When running morseexe.py it will translate the message you input into morse code and it will display it with the LED repeatedly until you exit the program (CTRL C).
    - It will also print out the translated message in the console every time the LED finishes.
    - EXAMPLE: python3 morseexe.py Hello World will output ".... . .-.. .-.. --- / .-- --- .-. .-.. -.. / /". If you put this into a morse to text convert ([I suggest this one](https://morsecode.scphillips.com/translator.html)) it will give you "HELLO WORLD".
