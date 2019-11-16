import sqlite3 as s
con = s.connect('preeti_database.db')
with con:
    cur=con.cursor()
    cur.execute("Create table if not exists details(fname text not null,lname text,email text primary key not null,password text not null,weight int not null,height int not null,profession text,gender text)")
    cur.execute("""Select * from details""")
    l=cur.fetchall()
    print(l)
