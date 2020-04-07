from dotDash import *

def a():
    dot()
    dash()

def b():
    dash()
    dot()
    dot()
    dot()

def c(): 
    dash()
    dot()
    dash()
    dot()

def d():
    dash()
    dot()
    dot()

def e():
    dot()

def f():
    dot()
    dot()
    dash()
    dot()

def g():
    dash()
    dash()
    dot()

def h():
    dot()
    dot()
    dot()
    dot()

def i():
    dot()
    dot()

def j():
    dot()
    dash()
    dash()
    dash()

def k():
    dash()
    dash()

def l():
    dot()
    dash()
    dot()
    dot()
def m():
    dash()
    dash()

def n():
    dash()
    dot()

def o():
    dash()
    dash()
    dash()

def p():
    dot()
    dash()
    dash()
    dot()

def q():
    dash()
    dot()
    dash()
    dash()

def r():
    dot()
    dash()
    dot()

def s():
    dot()
    dot()
    dot()

def t():
    dash()

def u():
    dot()
    dot()
    dash()

def v():
    dot()
    dot()
    dot()
    dash()

def w():
    dot()
    dash()
    dash()

def x():
    dash()
    dot()
    dot()
    dash()

def y():
    dash()
    dot()
    dash()
    dash()

def z():
    dash()
    dash()
    dot()
    dot()

def texttomorse(message):
    message = message.lower()
    message = message.split()
    spacedmessage = ''
    for word in message:
        word = word + '//'
        spacedmessage = spacedmessage + word
    spacedmessage = spacedmessage.split('/')
    for word in spacedmessage:
        if word=='': word = '/'
        for letter in word:
            if letter in 'a b c d e f g h i j k l m n o p q r s t u v w x y z':
                globals()[letter]()
            if letter=='/': space()
            if not letter=='/':
                letterspace()
    print('')
