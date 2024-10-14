#P07_main.py
from mypack.saluti.hello import saluta
from mypack.matematica.operazioni import somma

def main():
    saluta("Mario")
    
    s = somma(10, 23)
    print(s)

if __name__ == "__main__":
    main()
