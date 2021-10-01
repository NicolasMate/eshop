import argparse
from user_table import UserTable
from utils import name_type, year_type, password_type, email_type, id_type, phone_type
# Main table from where we are working
# Start by writing python oop.py table(user,order,item) and action(add,modify,delete,list) and additional arguments
# Example: python oop.py user add --name="Karel" --surname="Máj" --phone="+420123456789" --email="old@shuterhand.com"
# --password="1saUUd" --year=1987
# Be careful leave spaces between each positional and optional arguments
USER_COLUMN_LIST = ["name", "surname", "phone", "year", "email", "password"]
DB_NAME = 'shopik.db'

parser = argparse.ArgumentParser()
parser.add_argument(
    "table", help="Table name", type=str, choices=["user", "order", "item"])
parser.add_argument(
    "action", help="Action name ", type=str, choices=["list", "add", "modify", "delete"])
parser.add_argument("--name", help="Name", type=name_type)
parser.add_argument("--surname", help="Surname", type=name_type)
parser.add_argument("--phone", help="Phone", type=phone_type)
parser.add_argument("--year", help="Year", type=year_type)
parser.add_argument("--email", help="Email", type=email_type)
parser.add_argument("--password", help="Password", type=password_type)
parser.add_argument("--id", help="Id", type=id_type)
args = parser.parse_args()
print(f"Table name {args.table}")
print(f"Action name {args.action}")

if args.table == "user":
    user_object = UserTable(DB_NAME)
    user_object.create_table()
    if args.action == "add":
        for column in USER_COLUMN_LIST:
            if not getattr(args, column, None):
                print(f"ERROR You need to specify {column}")
                exit(1)
        user_object.user_add(
            args.name, args.surname, args.phone, args.year, args.email, args.password
        )
    elif args.action == "list":
        user_object.list()
    elif args.action == "modify":
        if not args.id:
            print("ERROR You need to specify id")
            exit(1)
        column_dict = {}
        for column in USER_COLUMN_LIST:
            if getattr(args, column, None):
                column_dict[column] = getattr(args, column, None)
        user_object.modify(args.id, **column_dict)
    elif args.action == "delete":
        if not args.id:
            print("ERROR You need to specify id")
            exit(1)
        user_object.delete(args.id)
if args.table == "order":
    print("Not specified yet")
if args.table == "item":
    print("Not specified yet")
