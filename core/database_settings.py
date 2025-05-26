from typing import Optional, Union
import psycopg2
from core.config import DB_CONFIG



class DatabaseManager:
    def __init__(self):
         self.conn: Optional[psycopg2.extensions.connection] = None
         self.conn: Optional[psycopg2.extensions.cursor] = None

    
    def __enter__(self):
         self.conn = psycopg2.connect(**DB_CONFIG)
         self.cursor = self.conn.cursor(cursor_factory=DictCursor)
         return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
              self.conn.rollback()
        else:
             self.conn.commit()
    
        if self.conn:
             self.conn.close()

        if self.cursor:
             self.cursor.close()


    def execute(self, query: str, params: Union[tuple, dict, None] = None):
         self.cursor.execute(query, params)


    def fetchone(self, query: str, params: Union[tuple, dict, None] = None):
         self.cursor.execute(query, params)
         return self.cursor.fetchone()


    def fetchall(self, query: str, params: Union[tuple, dict, None] = None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()


def execute_query(
           query: str, 
           params: Union[tuple, dict, None] = None
           fatch: Union[str, None] = None
) -> None | DictRow | Union[tuple, dict, None]

