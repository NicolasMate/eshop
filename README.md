# Start by writing python oop.py table(user,order,item) and action(add,modify,delete,list) and additional arguments
# USER table
# Data used for our´s shop users are stored in file shopik.db, if not existing this file is created automatically
# For adding user we simply use table user and action add and we have to write all optional arguments for table user (name, surname, phone, year, email, password), except for id which is generated automatically, we can not have null values inside arguments or user will not be added into our database
# Example adding user: python oop.py user add --name="Karel" --surname="Máj" --phone="+420123456789" --email="old@shuterhand.com" --password="1saUUd" --year=1987
# Example listing users: python oop.py user list
# Example deleting user: python oop.py user delete --id=4
# Example modifiing user: python oop.py user modify --id=6 --name="Karel"
# Be careful leave spaces between each positional and optional arguments

