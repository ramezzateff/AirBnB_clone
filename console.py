# #!/usr/bin/python3
# 'Module for the entry  interpreter'

# import models
# from models.base_model import BaseModel
# import cmd
# from models import storage
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
# class HBNBCommand(cmd.Cmd):
#     'its my interpreter'
#     prompt = '(hbnb)'
#     def do_quit(self, arg):
#         'Quit command to exit the program'
#         return True
#     def do_EOF(self, arg):
#         'for handle end line'
#         print()
#         return True
#     def emptylines(self):
#         'empty lin + != anything'
#         return ''

#     def do_create(self, arg):
#         """Creates a new instance of BaseModel, saves it, and prints the id"""
#         args = arg.split()
#         if len(args) == 0:
#             print("** class name missing **")
#             return
#         class_name = args[0]
#         if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
#             print("** class doesn't exist **")
#             return
#         new_instance = eval(class_name)()
#         new_instance.save()
#         print(new_instance.id)



# if __name__ == '__main__':
#     HBNBCommand().cmdloop()
