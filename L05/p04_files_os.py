import os
import time

#creo un file
file = open("error.txt", "w")
file.close()

#faccio una pausa
time.sleep(5)

#cancello il file
os.remove("error.txt")
