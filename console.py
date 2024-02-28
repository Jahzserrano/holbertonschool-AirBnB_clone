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

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        instance_id = arg[1]
        try:
            instance = BaseModel.get(instance_id)
            print(instance)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the name class and id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        instance_id = arg[1]
        try:
            instance = BaseModel.get(instance_id)
            instance.delete()
            BaseModel.save()
            print(instance)
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all the string representation of all instances"""
        if arg not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        instances = BaseModel.all()
        print([str(instances) for instance in instances])

    def do_update(self, arg):
        """Updates an instance"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        instance_id = arg[1]
        try:
            instance = BaseModel.get(instance_id)
            if len(arg) < 4:
                print("** attributr name missing **")
                return
            attr_name = arg[2]
            attr_value = arg[3]
            settattr(instance, attr_name, attr_value)
            instance.save()
        except KeyError:
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
