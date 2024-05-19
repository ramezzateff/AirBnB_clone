#!/usr/bin/python3
'Module for the entry  interpreter'
import cmd
from models.base_model import BaseModel
class HBNBCommand(cmd.Cmd):
    'its my interpreter'
    prompt = '(hbnb)'
    def do_quiet(self, arg):
        'Quit command to exit the program'
        return True
    def do_EOF(self, arg):
        'for handle end line'
        print()
        return True
    def emptylines(self):
        'empty lin + != anything'
        return ''
    def do_creat(self, arg):
        'creat new instance, save Json and print id'
        if arg == '':
            print("** class name missing **")
        if arg not in BaseModel:
            print("create MyModel")
        else:
            new_instannce = BaseModel()
            new_instannce.save()
            print(new_instannce.id)





if __name__ == '__main__':
    HBNBCommand().cmdloop()
