from morse import *

def a():
    try:
        dot()
        dash()
    except NameError:
        pass

def b():
    try:
        dash()
        dot()
        dot()
        dot()
    except NameError:
        pass

def c():
    try:
        dash()
        dot()
        dash()
        dot()
    except NameError:
        pass

def d():
    try:
        dash()
        dot()
        dot()
    except NameError:
        pass

def e():
    try:
        dot()
    except NameError:
        pass

def f():
    try:
        dot()
        dot()
        dash()
        dot()
    except NameError:
        pass

def g():
    try:
        dash()
        dash()
        dot()
    except NameError:
        pass

def h():
    try:
        dot()
        dot()
        dot()
        dot()
    except NameError:
        pass

def i():
    try:
        dot()
        dot()
    except NameError:
        pass

def j():
    try:
        dot()
        dash()
        dash()
        dash()
    except NameError:
        pass

def k():
    try:
        dash()
        dot()
        dash()
    except NameError:
        pass

def l():
    try:
        dot()
        dash()
        dot()
        dot()
    except NameError:
        pass

def m():
    try:
        dash()
        dash()
    except NameError:
        pass

def n():
    try:
        dash()
        dot()
    except NameError:
        pass

def o():
    try:
        dash()
        dash()
        dash()
    except NameError:
        pass

def p():
    try:
        dot()
        dash()
        dash()
        dot()
    except NameError:
        pass

def q():
    try:
        dash()
        dot()
        dash()
        dash()
    except NameError:
        pass

def r():
    try:
        dot()
        dash()
        dot()
    except NameError:
        pass

def s():
    try:
        dot()
        dot()
        dot()
    except NameError:
        pass

def t():
    try:
        dash()
    except NameError:
        pass

def u():
    try:
        dot()
        dot()
        dash()
    except NameError:
        pass

def v():
    try:
        dot()
        dot()
        dot()
        dash()
    except NameError:
        pass

def w():
    try:
        dot()
        dash()
        dash()
    except NameError:
        pass

def x():
    try:
        dash()
        dot()
        dot()
        dash()
    except NameError:
        pass

def y():
    try:
        dash()
        dot()
        dash()
        dash()
    except NameError:
        pass

def z():
    try:
        dash()
        dash()
        dot()
        dot()
    except NameError:
        pass

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
                eval(letter + '()')
            if letter=='/': space()
            if not letter=='/':
                letterspace()
    print('')
