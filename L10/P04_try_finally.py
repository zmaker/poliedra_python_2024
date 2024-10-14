try:
    f = open("readme.txt", 'r')
    #operazioni sul file
except:
    print("errore file")
    
finally:
    f.close()