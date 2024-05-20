#!/usr/bin/python3
'Module for the entry  interpreter'
import cmd
import models
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
    def do_create(self, arg):
        'creat new instance, save Json and print id'
        if arg == '' or arg == None:
            print("** class name missing **")
        # elif type(arg).__name__ != BaseModel:
        #     print("** class doesn't exist **")
        else:
            new_instannce = models.storage()
            new_instannce.save()
            print(new_instannce.id)





if __name__ == '__main__':
    HBNBCommand().cmdloop()
