import sqlite3

with sqlite3.connect("database.db") as c:
    cur = c.cursor()
    
    while True:
        name = input("nome: ")
        qty = int(input("qty: "))
        price = float(input("price: "))
        
        cid = "(select max(CID) + 1 as newcid from coffee)"
    
        sql = f"insert into coffee (CID,NAME,QTY,PRICE) values "\
              f"( {cid}, '{name}', {qty}, {price} )"
        print(sql)
        input("premi invio per inserire i dati")
        cur.execute(sql)
        c.commit()
        
        ans = input("ancora (s/n)? ")
        if not ans == 's':
            break
        
    print("Bye!")
