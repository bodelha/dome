import psycopg2
from psycopg2 import sql
import os
from utils import logger


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.database_url = os.getenv("DATABASE_URL")
            self.conn = None
            self.initialized = True

    def connect(self):
        if not self.conn or self.conn.closed:
            try:
                self.conn = psycopg2.connect(self.database_url)
                logger.debug("Connected to PostgreSQL database!")
            except (Exception, psycopg2.Error) as error:
                logger.error("Error connecting to PostgreSQL database:", error)
                raise

    def execute(self, query, params=None):
        if not self.conn or self.conn.closed:
            self.connect()
        cursor = self.conn.cursor()
        logger.debug("Executing query: %s with: %s", query, params)
        cursor.execute(query, params)
        return cursor

    def fetchall(self, query, params=None):
        cursor = self.execute(query, params)
        results = cursor.fetchall()
        cursor.close()
        return results

    def fetchone(self, query, params=None):
        cursor = self.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            logger.debug("Connection to PostgreSQL database closed.")
