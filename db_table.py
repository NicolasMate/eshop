import sqlite3

# here are main functions that we need for operating our program
class DBTable:
    # Constructor
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        self.con.row_factory = sqlite3.Row

    def get_cursor(self):
        cur = self.con.cursor()
        return cur

    def execute_query(self, query, data_tuple=()):
        cur = self.get_cursor()
        res = cur.execute(query, data_tuple)
        return res

    # Save (commit) the changes
    def commit(self):
        self.con.commit()

    # Destructor
    def __del__(self):
        if self.con:
            self.con.close()
