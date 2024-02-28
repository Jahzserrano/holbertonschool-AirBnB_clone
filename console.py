#!/usr/bin/python3
"""Defining HBNBCommand class"""
import cmd
import json

from numpy import save
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Custom command interpreter for HBNB project."""

    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

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

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)
    
    def show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **") 


if __name__ == "__main__":
    HBNBCommand().cmdloop()
