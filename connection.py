import psycopg2

from psycopg2.extras import DictCursor

db_config = {
    "database": "products",
    "user": "products_user",
    "host": "localhost",
    "port": "5432",
    "password": "product_password"
}

conn = psycopg2.connect(**db_config)
cursor = conn.cursor(cursor_factory = DictCursor)
 
cursor.execute(
    query = '''
    SELECT * FROM test1;
    '''
)
# conn.commit()
print(cursor.fetchall())
print("done")