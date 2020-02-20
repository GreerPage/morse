<h1>Morse Code for Raspberry Pi</h1>

This project is meant be run strictly on a Raspberry Pi. It assumes that you have an LED connected and properly wired to a breadboard using GPIO pin 18 <a href="https://cdn.shopify.com/s/files/1/0176/3274/files/LEDs-BB400-1LED_bb_grande.png?6398700510979146820">see this link</a>.

To run: run morseexe.py, it takes one argument which is the message to be translated. EXAMPLE: python3 morseexe.py Hello World

<h2>Breakdown of the project:</h2>
<ul>
  <li>morse.py = defines the dot dash and space functions that are used to trigger or not trigger the led for the certain amount of time</li>
  <li>morseKey.py = defines functions for all of the letters. For example it says that for the letter "e" do one dot. This is all brought together in the texttomorse function, which takes one argument which is the message to be translated.</li>
  <li>morseexe.py = this takes a command line argument of the message you want to translate. It is the runner for the full project.</li>
</ul>
<h2>What it does:</h2>
<ul>
  <li>When running morseexe.py it will translate the message you input into morse code and it will display it with the LED repeatedly until you exit the program (CTRL C).</li>
  <li>It will also print out the translated message in the console every time the LED finishes.</li>
  <li>EXAMPLE: python3 morseexe.py Hello World will output ".... . .-.. .-.. --- / .-- --- .-. .-.. -.. / /". If you put this into a morse to text converter <a href="https://morsecode.scphillips.com/translator.html">I suggest this one</a> it will give you "HELLO WORLD".</li>
</ul>
