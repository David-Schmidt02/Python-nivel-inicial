import sqlite3

##INSERCION EN LA BASE
con = sqlite3.connect("mibase.db")
cursor1 = con.cursor()
sql = "CREATE TABLE futbol(id integer PRIMARY KEY AUTOINCREMENT , Pais text, WC text, Posicion text);"
cursor1.execute(sql)
con.commit()
con.close()
