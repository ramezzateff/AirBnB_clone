#!/usr/bin/python3
'Module for the entry  interpreter'
import re
import cmd
import json
from models import storage
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """its my interpreter"""
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """for handle end line"""
        print()
        return True

    def emptylines(self):
        """empty lin + != anything"""
        pass

    def do_create(self, arg):
        """Creates an instance"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_create = storage.classes()[arg]()
            new_create.save()
            print(new_create.id)

    def do_show(self, arg):
        """reper instance"""
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            word = arg.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = f"{word[0]}.{word[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        """Split the argument into word"""
        word = arg.split(" ")
        all_objects = storage.all().items()
        if arg != "" and word[0] in storage.classes():
            inst_list = [str(obj) for key, obj in storage.all().items() if type(obj).__name__ == word[0]]
        else:
            """Create a list of string representations of all instances"""
            print("** class doesn't exist **")
            inst_list = [str(obj) for key, obj in all_objects]

        print(inst_list)

    def update_dict(self, classname, uid, s_dict):
        """Helper update"""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()
                
    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file
        """
        if arg == "" or arg is None:
            print("** class name missing **")
            return

        re_m = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(re_m, arg)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


    def do_count(self, arg):
        """times  instances"""
        word = arg.split(" ")
        if not word[0]:
            print("** class name missing **")
        elif word[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            cou = [key for key in storage.all() if key.startswith(word[0] + ".")]
            print(len(cou))

if __name__ == "__main__":
    HBNBCommand().cmdloop()
