from primalib import hello
from primalib import salutoConNome as saluto2
#import primalib
import primalib as pl

from time import sleep as pausa

def main():
    #primalib.hello()
    hello()
    saluto2('mario')
    pausa(2)
    s = pl.somma(10, 20)
    print(s)

if __name__ == '__main__':
    main()