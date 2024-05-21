#!/usr/bin/python3
'Module for the entry  interpreter'
import cmd
import json
import models
from models import storage
# from models.base_model import BaseModel

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
                print("** instance id missing **")
            else:
                key = f"{word[0]}.{word[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            word = arg.split(" ")
            if word[0] not in storage.classes():
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
            inst_list = [str(obj) for key, obj in all_objects if type(obj).__name__ == word[0]]
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
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        classname, uid, attribute, value = args[0], args[1], args[2], args[3]

        if classname not in storage.classes():
            print("** class doesn't exist **")
            return

        key = f"{classname}.{uid}"
        if key not in storage.all():
            print("** no instance found **")
            return
    
        """If the attribute is empty, print an error message and return"""
        if not attribute:
            print("** attribute name missing **")
            return

        if not value:
            print("** value missing **")
            return

        if '"' not in value:
            value = float(value) if '.' in value else int(value)
        else:
            value = value.replace('"', '')

        """Get the attributes of the classname from the storage"""
        attributes = storage.attributes()[classname]
        if attribute in attributes:
            value = attributes[attribute]

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
