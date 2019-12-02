# Morse Code for Raspberry Pi

This program is meant be run strictly on a Raspberry Pi. It assumes that you have an LED connected to GPIO pin 18. To change the GPIO pin you can edit it in morse.py

To run: run morseexe.py, it takes one argument which is the message to be translated this should be a string. EXAMPLE: python3 morseexe.py "Hello World"

### Breakdown of the program:
  - morse.py = defines the dot dash and space functions that are used to trigger or not trigger the led for the certain amount of time
