# Morse Code for Raspberry Pi

(Only works on raspis)


## Installation
```bash
$ git clone https://github.com/GreerPage/morse
$ cd morse
$ pip install .
```
make sure to connect an LED to a raspberry pi as shown below:

![raspi](https://greerpage.com/static/images/raspidiagram.png)

## Usage
```bash
$ morse hello, world! #displays hello, world! in morse code once
$ morse hello, world! -l true #displays hello, world! in morse code until loop is stopped 
```

## License
MIT License