from sys import argv
import primalib as pl

def main(argv):
    if len(argv) == 4:
        A = int(argv[1])
        B = int(argv[3])
        op = argv[2]
        res = 0
        if op == '+':
            res = pl.somma(A, B)
        elif op == '-':
            res = pl.diff(A, B)
        elif op == 'x':
            res = pl.prod(A, B)
        elif op == ':':
            res = pl.div(A, B)
        else:
            print("op. consentite: + - x : ")
        print(res)
        
    else:
        print("parametri insuff.")
        print("op: + - x : ")
        print("es: 10 + 2")
    

if __name__ == "__main__":    
    main(argv)