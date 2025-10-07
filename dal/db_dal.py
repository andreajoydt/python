import sqlite3
# from abc import ABC

class DbDaoABC:

    def __get_db_connection(self):
        return sqlite3.connect("contacts.db")

    def execute_select(self, sql):
        cnn = self.__get_db_connection()
        return cnn.execute(sql)