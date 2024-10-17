import sqlite3

#c = sqlite3.connect("database.db")
#c.close()

with sqlite3.connect("database.db") as c:
    cur = c.cursor()
    
    cid = int(input("id del record da cancellare: "))
    
    ans = input("sicuro (s/n)? ")
    if ans == 's':
        sql = f"DELETE FROM coffee WHERE cid = {cid}"
        print(sql)
        
        input("premi invio")
        
        cur.execute(sql)
        c.commit()
    