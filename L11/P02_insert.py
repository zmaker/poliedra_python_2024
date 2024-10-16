import sqlite3

#c = sqlite3.connect("database.db")
#c.close()

with sqlite3.connect("database.db") as c:
    cur = c.cursor()
    
    while True:
        cid = int(input('cid: '))
        name = input("nome: ")
        qty = int(input("qty: "))
        price = float(input("price: "))
    
        sql = f"insert into coffee (CID,NAME,QTY,PRICE) values "\
              f"( {cid}, '{name}', {qty}, {price} )"
        print(sql)
        cur.execute(sql)
        #c.commit()
        
        ans = input("ancora (s/n)? ")
        if not ans == 's':
            break
        
    #c.commit()
    print("Bye!")