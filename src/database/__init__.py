import sqlite3

with sqlite3.connect('src/database/model.db') as db:
        cursor = db.cursor()

def create_db():
    cursor.execute('''create table if not exists grupo(id integer primary key autoincrement, name text not null, tag text not null, number_of_users integer)''') 

from .import create_db