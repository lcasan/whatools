import sqlite3

def create_db():
    with sqlite3.connect('src/database/model.db') as db:
        cursor = db.cursor()
    
    cursor.execute('''create table if not exists stocks(id integer primary key autoincrement, name text not null, tag text not null, number_of_users integer)''')  