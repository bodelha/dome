import psycopg2
from psycopg2 import sql
import os
from utils import logger


class Database:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")
        self.conn = None

    def connect(self):
        if not self.conn:
            try:
                self.conn = psycopg2.connect(self.database_url)
                logger.info("Connected to PostgreSQL database!")
            except (Exception, psycopg2.Error) as error:
                logger.error("Error connecting to PostgreSQL database:", error)
                raise

    def execute(self, query, params=None):
        if not self.conn:
            self.connect()
        with self.conn.cursor() as cursor:
            logger.debug("Executing query: %s with: %s", query, params)
            cursor.execute(query, params)
            return cursor

    def fetchall(self, query, params=None):
        logger.debug("Fetchall: %s with: %s", query, params)
        with self.execute(query, params) as cursor:
            return cursor.fetchall()

    def fetchone(self, query, params=None):
        logger.debug("Fetchone: %s with: %s", query, params)
        with self.execute(query, params) as cursor:
            return cursor.fetchone()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            logger.info("Connection to PostgreSQL database closed.")
