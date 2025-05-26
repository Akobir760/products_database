products = """
    CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL UNIQUE,
    quantity VARCHAR (128) NOT NULL,
    status BOOLEAN DEFAULT FALSE
)"""