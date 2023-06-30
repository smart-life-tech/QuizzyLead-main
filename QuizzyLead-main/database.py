import sqlite3
from flask import g
import os

def connect_to_DB():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(current_dir, "app_database.db")
    sql = sqlite3.connect(db_file)
    sql.row_factory = sqlite3.Row
    return sql

    
    
def getDatabase():
    if not hasattr(g, "app_database_db"):
        g.app_database_db = connect_to_DB()
    return g.app_database_db