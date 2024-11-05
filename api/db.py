import psycopg2
import os

class Database:
    def __init__(self):
        self.database_url = os.environ.get('DATABASE_URL')
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(self.database_url)
            print("Connected to PostgreSQL database!")
        except (Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL database:", error)
            raise

    def execute(self, query, params=None):
        if self.conn is None:
            self.connect()

        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor

    def fetchall(self, query, params=None):
        cursor = self.execute(query, params)
        return cursor.fetchall()

    def fetchone(self, query, params=None):
        cursor = self.execute(query, params)
        return cursor.fetchone()

    def close(self):
        if self.conn is not None:
            self.conn.close()
            print("Connection to PostgreSQL database closed.")
