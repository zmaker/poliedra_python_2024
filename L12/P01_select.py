import sqlite3

c = sqlite3.connect("database.db")

sql = "select * from coffee"

cur = c.cursor()
cur.execute(sql)

totale_magazzino = 0 
for row in cur.fetchall():
    parziale = row[2]*row[3]
    totale_magazzino += parziale
    print(f"({row[0]}) - {row[1]}\tq: {row[2]}\tp: {row[3]}\tt:{parziale}")

print(f"\nTOT: {totale_magazzino}")
c.close()