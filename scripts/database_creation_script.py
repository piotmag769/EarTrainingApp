import sqlite3

connector = sqlite3.connect('../main_database')
cursor = connector.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL,
        PRIMARY KEY (username)
        )
        ''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS Types(
        main_category VARCHAR(15) NOT NULL,
        ex_type VARCHAR(15) NOT NULL,
        PRIMARY KEY (ex_type)
        )
        ''')

cursor.execute('''
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

cursor.execute('''INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '2_m')''')
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '2_w')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '3_m')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '3_w')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '4')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '4_5_tryt')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '5')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '6_m')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '6_w')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '7_m')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '7_w')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('INTERVALS', '8')")


cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'dur_z')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'dur_6')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'dur_64')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'mol_z')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'mol_6')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'mol_64')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'zmn_z')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'zmn_6')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'zmn_64')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('TRIADS', 'zwiek')")

cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('DOMINANT_7TH', 'zas')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('DOMINANT_7TH', '1_kw_sek')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('DOMINANT_7TH', '2_ter_kw')")
cursor.execute("INSERT INTO Types(main_category, ex_type) VALUES('DOMINANT_7TH', '3_sek')")

connector.commit()
cursor.close()

