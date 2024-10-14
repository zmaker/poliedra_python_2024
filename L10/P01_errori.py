#print(x)

#x = 0
#if (x > 0):
#    print(x)

#n = 10
#for i in range(10):
#    r = n/(i-5)
#    print(i, r)

# https://docs.python.org/3/library/exceptions.html

import time
count = 0

while (True):
    print(f"elaborazione n.: {count}")
    time.sleep(1)
    count += 1
    try:
        print(conteggio)
#    except Exception as e:
#        print("errore di stampa")
#        print(e.__class__)
    except NameError:
        print("var non def")
    except (TypeError, ZeroDivisionError):
        print("err2")