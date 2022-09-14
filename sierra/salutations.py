import os

from golf import greetings


def salutation():
    greet = greetings.greet()
    return '%s%s Have a nice day!' % (greet, os.linesep)