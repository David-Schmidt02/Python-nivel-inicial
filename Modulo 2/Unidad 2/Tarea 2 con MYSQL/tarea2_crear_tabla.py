import mysql.connector

mibase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tarea2_sql",
)
mi_cursor = mibase.cursor()
mi_cursor.execute(
    "CREATE TABLE futbol(id INT(5) NOT NULL PRIMARY KEY AUTO_INCREMENT, Pais VARCHAR(15),WC INT(100), Posicion VARCHAR(30))"
)
