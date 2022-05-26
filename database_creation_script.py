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
        ex_id INTEGER NOT NULL,
        is_correct INTEGER NOT NULL,
        username VARCHAR(50),
        instrument VARCHAR(15),
        mode VARCHAR(15),
        ex_type VARCHAR(15),
        done_date DATE,
        PRIMARY KEY (ex_id),
        FOREIGN KEY (username)
            REFERENCES Users (username),
        FOREIGN KEY (ex_type)
            REFERENCES Types (ex_type)
        )
        ''')

c.execute('''INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '2_m')''')
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '2_w')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '3_m')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '3_w')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '4')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '4_5_tryt')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '5')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '6_m')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '6_w')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '7_m')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '7_w')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '8')")


c.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'dur_z')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'dur_6')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'dur_64')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'mol_z')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'mol_6')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'mol_64')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'zmn_z')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'zmn_6')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'zmn_64')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'zwiek')")

c.execute("INSERT INTO Types(main_category, ex_type) VALUES('DOMINANT_7TH', 'zas')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('DOMINANT_7TH', '1_kw_sek')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('DOMINANT_7TH', '2_ter_kw')")
c.execute("INSERT INTO Types(main_category, ex_type) VALUES('DOMINANT_7TH', '3_sek')")



