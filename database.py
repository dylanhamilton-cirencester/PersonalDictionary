import sqlite3

class DictionaryDB():

    def __init__(self):
        self.con = sqlite3.connect("dictionary.db")

    def create_db(self):
        cur = self.con.cursor()

        cur.execute("CREATE TABLE dictionary(word TEXT PRIMARY KEY, " \
                    "origin TEXT)")
        cur.execute("CREATE TABLE phonetic()")