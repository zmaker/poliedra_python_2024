import random

f = open("log.txt", 'a')
val = random.randint(0,100)
f.write(f"temp={val}\n")
f.close()