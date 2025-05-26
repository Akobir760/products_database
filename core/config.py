from dotenv import load_dotenv
import os

load_dotenv(
    dotenv_path="./.env"
)

DB_NAME = os.getenv("PDB_NAME")
DB_USER = os.getenv("PDB_USER")
DB_PASS = os.getenv("PDB_PASS")
DB_HOST = os.getenv("PDB_HOST")
DB_PORT = os.getenv("PDB_PORT")

DB_CONFIG = {
    "database":     DB_NAME,
    "user": DB_USER,
    "host": DB_HOST,
    "port": DB_PORT,
    "password": DB_PASS
}