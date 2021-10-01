# Start by writing python oop.py table(user,order,item) and action(add,modify,delete,list) and additional arguments
# USER table
# Data used for our´s shop users are stored in file shopik.db, if not existing this file is created automatically
# For adding user we simply use table user and action add and we have to write all optional arguments for table user (name, surname, phone, year, email, password), except for id which is generated automatically, we can not have null values inside arguments or user will not be added into our database
# Example adding user: python oop.py user add --name="Karel" --surname="Máj" --phone="+420123456789" --email="old@shuterhand.com" --password="1saUUd" --year=1987
# Listing action will list all current users in our shopik.db file
# Example listing users: python oop.py user list, side note passwords are visible only hashed
# If we need to delete user we need to know his id then we can simply delete him by calling delete action with his id
# Example deleting user: python oop.py user delete --id=4
# Modifiing action is very similar to delete acion however we also have to specify which addional arguments are to be changed, unspecified arguments will remain same
# Example modifiing user: python oop.py user modify --id=6 --name="Karel"
# Before: "id": 6, "name": "Radim", "surname": "Uzel", "phone": "434345543", "year": 2000, "email": "adsgg@ddda.com", "password": "44478bf7433e49d8e48dcd6069ad8cab18711fd30bb1
2bdc394346cbb30254ec"
# After: "id": 6, "Karel": "Radim", "surname": "Uzel", "phone": "434345543", "year": 2000, "email": "adsgg@ddda.com", "password": "44478bf7433e49d8e48dcd6069ad8cab18711fd30bb1
2bdc394346cbb30254ec"
# Be careful leave spaces between each positional and optional arguments
# add, delete, modify actions automatically commit upon successful completion of the command 

