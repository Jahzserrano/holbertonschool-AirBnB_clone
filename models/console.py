#!/usr/bin/python3

import cmd

"""Defining HBNBCommand class"""

class HBNBCommand(cmd.Cmd):
    """Custom command interpreter for HBNB project."""
    
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Exit the program."""
        return True
    
    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)."""
        print("\nGoodbye!")
        return True
    
    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
