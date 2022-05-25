import sqlite3

conn = sqlite3.connect('main_database')
c = conn.cursor()

c.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL,
        PRIMARY KEY (username)
        )
        ''')

c.execute('''
        CREATE TABLE IF NOT EXISTS Types(
        main_category VARCHAR(15) NOT NULL,
        ex_type VARCHAR(15) NOT NULL,
        PRIMARY KEY (ex_type)
        )
        ''')

c.execute('''
        CREATE TABLE IF NOT EXISTS Scores(
        all_tries INTEGER NOT NULL,
        correct_tries INTEGER NOT NULL,
        username VARCHAR(50),
        instrument VARCHAR(15),
        mode VARCHAR(15),
        ex_type VARCHAR(15),
        PRIMARY KEY (username, instrument, mode, ex_type),
        FOREIGN KEY (username)
            REFERENCES Users (username),
        FOREIGN KEY (ex_type)
            REFERENCES Types (ex_type)
        )
        ''')
