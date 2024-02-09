import sqlite3
con = sqlite3.connect("sqlite.db")
con.execute('''
    CREATE table teacher (
            teacher_id int PRIMARY KEY, 
            teacher_name varchar(50), 
            teacher_age varchar(5),
            teacher_gender varchar(25),
            teacher_date_of_birth varchar(25)
    )
''')
con.close()