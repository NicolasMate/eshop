import sqlite3


# here are main functions that we need for operating our program
class DBTable:
    def __init__(self, db_name):
        """
        Constructor
        :param db_name:
        """
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

    def commit(self):
        """
        Save (commit) the changes
        """
        self.con.commit()

    def __del__(self):
        """
        Destructor
        """
        if self.con:
            self.con.close()
