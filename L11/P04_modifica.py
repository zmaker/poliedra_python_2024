import sqlite3

def rowExist(cursor, idriga):
    sql = f"select count(*) as numrighe from coffee where CID = {idriga}"    
    cursor.execute(sql)
    numrighe = 0
    for row in cur.fetchall():
        numrighe = row[0]
    if numrighe > 0:
        return True
    else:
        return False

    

with sqlite3.connect("database.db") as c:
    cur = c.cursor()
    
    cid = int(input("Id del record da modificare: "))
    
    if rowExist(cur, cid):
        price = float(input("nuovo prezzo: "))
        qty = int(input("nuova quantita: "))
        
        if price < 0.0:
            price = 0.0
        if qty < 0:
            qty = 0
        
        sql = f"UPDATE coffee SET price = {price}, qty = {qty} WHERE CID = {cid}"
        print(sql)
        
        input("premi invio")
        cur.execute(sql)
        c.commit()
    
        print("modifica effettuata")
    else:
        print("riga non trovata")
        
        