from sys import argv
from calclib import Calc

def main():
    parms = argv
    if not len(parms) == 4:
        print("Parametri non corretti! calc 10 + 20")
    else:
        c = Calc()
        c.setOperando1(parms[1])
        c.setOperando2(parms[3])
        c.setOperazione(parms[2])
        ans = c.getResult()
        #print(ans)
        print(c)

if __name__ == "__main__":
    main()