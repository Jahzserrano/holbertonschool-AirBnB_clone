#!/usr/bin/python3
"""Defining HBNBCommand class"""
import cmd
import json

from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Custom command interpreter for HBNB project."""

    __classes = {
        "BaseModel": BaseModel
        }

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
        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_instances = storage.all(args[0])
        instance_key = "{}.{}".format(args[0], instance_id)
        if instance_key in all_instances:
            print(all_instances[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the name class and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_instances = storage.all(args[0])
        instance_key = "{}.{}".format(args[0], instance_id)
        if instance_key in all_instances:
            print(all_instances[instance_key])
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all the string representation of all instances"""
        objdict = storage.all()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instances = [str(obj) for key, obj in objdict.items()
                         if key.split('.')[0] == args[0]]
            print(instances)

    def do_update(self, arg):
        """Updates an instance"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_instances = storage.all(args[0])
        instance_key = "{}.{}".format(args[0], instance_id)
        if instance_key in all_instances:
            if len(args) < 4:
                print("** attribute name missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            setattr(all_instances[instance_key], attr_name, attr_value)
            all_instances[instance_key].save()
        else:
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
