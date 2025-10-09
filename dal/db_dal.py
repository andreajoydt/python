import sqlite3

class DbDaoABC:

    def __get_db_connection(self):
        return sqlite3.connect('address_book.db')

    def execute_select(self, sql):
        cnn = self.__get_db_connection()
        return cnn.execute(sql)