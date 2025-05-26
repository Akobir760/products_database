from typing import Optional
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
