from .key import *
from .lights import off

def char_to_morse(c):
    if c == 'a':
        a()
    elif c == 'b':
        b()
    elif c == 'c':
        c()
    elif c == 'd':
        d()
    elif c == 'e':
        e()
    elif c == 'f':
        f()
    elif c == 'g':
        g()
    elif c == 'h':
        h()
    elif c == 'i':
        i()
    elif c == 'j':
        j()
    elif c == 'k':
        k()
    elif c == 'l':
        l()
    elif c == 'm':
        m()
    elif c == 'n':
        n()
    elif c == 'o':
        o()
    elif c == 'p':
        p()
    elif c == 'q':
        q()
    elif c == 'r':
        r()
    elif c == 's':
        s()
    elif c == 't':
        t()
    elif c == 'u':
        u()
    elif c == 'v':
        v()
    elif c == 'w':
        w()
    elif c == 'x':
        x()
    elif c == 'y':
        y()
    elif c == 'z':
        z()
    elif c == '1':
        one()
    elif c == '2':
        two()
    elif c == '3':
        three()
    elif c == '4':
        four()
    elif c == '5':
        five()
    elif c == '6':
        six()
    elif c == '7':
        seven()
    elif c == '8':
        eight()
    elif c == '9':
        nine()
    elif c == '0':
        zero()
    elif c == '.':
        period()
    elif c == '?':
        question_mark()
    elif c == ',':
        comma()
    elif c == '!':
        exclamation_point()
    else:
        print('{}: unrecognized character'.format(c))
        off()
        exit()
    