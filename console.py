#!/usr/bin/python3
"""The module of a console"""


import cmd

class HBNBCommand(cmd.Cmd):
    """the console of airbnb"""
    prompt = '(hbnb) '

    def do_quit(self, arg: str):
        'Quit command to exit the program\n'
        return True
    def do_EOF(self, arg: str):
        'Exit the program'
        return True
    def emptyline(self) -> bool:
        False







if __name__ == '__main__':
    HBNBCommand().cmdloop()
