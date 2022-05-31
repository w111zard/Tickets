import sqlite3

class Database:
    def __init__ (self, file_name):
        try:
            self.connection = sqlite3.connect(file_name, check_same_thread=False)
            
        except sqlite3.Error as error:
            print(error)

    def execute_query_from_file(self, file_name):
        try:
            cursor = self.connection.cursor()
            queries = open(file_name).read().split(';')
            
            for query in queries:
                cursor.execute(query)
                
            self.connection.commit()

        except sqlite3.Error as error:
            print(error)

        finally:
            cursor.close()

    def select(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def execute(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        cursor.close()
