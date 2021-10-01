import hashlib
from db_table import DBTable
from utils import dict_from_row
import json
import sqlite3


# over here is main table for user table user functions

class UserTable(DBTable):
    def create_table(self):
        """
        Creating database file if not existing
        """
        q = 'CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, surname text, ' \
            'phone text, year int, email text, password text, CONSTRAINT unq_mail UNIQUE (email)); '
        self.execute_query(q)

    def check_user(self, user_id):
        """
        Function that check if user is existing based on id
        :param user_id:
        :return:
        """
        res = self.execute_query(f"SELECT count(*) FROM user WHERE id=?", user_id,)
        data = res.fetchone()[0]
        if data == 0:
            return False
        else:
            return True

    def user_add(self, name, surname, phone, year, email, password):
        """
        Function for adding user
        :param name:
        :param surname:
        :param phone:
        :param year:
        :param email:
        :param password:
        """
        print(f"Creating new user {name}, {surname}, {phone}, {year}, {email}")
        password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

        sqlite_insert_with_param = "INSERT INTO user (name, surname, phone, year, email, password) " \
                                   "VALUES (?, ?, ?, ?, ?, ?);"

        data_tuple = (name, surname, phone, year, email, password_hash)
        try:
            self.execute_query(sqlite_insert_with_param, data_tuple)
        except sqlite3.IntegrityError:
            print(
                f"User with the same email {email} already exists, if your wife does not have an email, "
                f"you are out of luck.")

        self.commit()

    def list(self):
        """
        Function for listing all users
        """
        query = 'select * from user;'
        res = self.execute_query(query)
        for row in res:
            json_string = json.dumps(dict_from_row(row), ensure_ascii=False)
            print(json_string)
        print("Listing all users")

    def delete(self, user_id):
        """
        Function for deleting user based on his id
        :param user_id:
        """
        user_exists = self.check_user(user_id)
        if user_exists:
            print(f"Deleting user with id {user_id}")
            self.execute_query(f"DELETE from user WHERE ID=?", (user_id))
            self.commit()
        else:
            print("Can not find user")
            exit(1)

    def modify(self, user_id, **kwargs):
        """
        Function for editing users using kwargs
        :param user_id:
        :param kwargs:
        """
        user_exists = self.check_user(user_id)
        if user_exists:
            print(f"Modifying user with id {user_id}")
            print("kwargs")
            for k, v in kwargs.items():
                print(f"kwargs[{k}]={v}")
                if k == "password":
                    password_hash = hashlib.sha256(v.encode("utf-8")).hexdigest()
                    print(f"SHA256({v})={password_hash}")
                    self.execute_query(f"UPDATE user SET {k}=? WHERE ID=?", (password_hash, user_id))
                else:
                    self.execute_query(f"UPDATE user SET {k}=? WHERE ID=?", (v, user_id))
            self.commit()
        else:
            print("Can not find user")
            exit(1)
