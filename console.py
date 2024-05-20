#!/usr/bin/python3
'Module for the entry  interpreter'
import cmd
from models.base_model import BaseModel
import models
from models import storage
class HBNBCommand(cmd.Cmd):
    'its my interpreter'
    prompt = '(hbnb)'
    def do_quit(self, arg):
        'Quit command to exit the program'
        return True
    def do_EOF(self, arg):
        'for handle end line'
        print()
        return True
    def emptylines(self):
        'empty lin + != anything'
        return ''

    def do_create(self, line):
        """Creates an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)
            print(b)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
