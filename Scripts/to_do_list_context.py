import mysql.connector


class ToDoListContext:
    def __init__(self, got_database='', got_host='localhost', got_user='root', got_password=''):
        self.connection_db = mysql.connector.connect(
            host=got_host,
            user=got_user,
            passwd=got_password,
            database=got_database
        )
        self.cursor_db = self.connection_db.cursor()

    def execute_database(self, got_sql, got_value=(), got_multi=False):
        self.cursor_db.execute(got_sql, got_value, got_multi)

    def fetchall_database(self):
        return self.cursor_db.fetchall()

    def fetchone_database(self):
        return self.cursor_db.fetchone()

    def commit_database(self):
        self.connection_db.commit()

    def close_database(self):
        self.connection_db.close()

    def create_database(self, database_name):
        sql = f'CREATE DATABASE IF NOT EXISTS {database_name};'
        self.execute_database(sql)
