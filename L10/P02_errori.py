while True:
    try:
        n = int(input("inserire un numero intero: "))
        if n == 99:
            break
        r = 100/n
        print(f"r = {r}")
    except ValueError:
        print("Non è un numero")
    except ZeroDivisionError:
        print("r = oo")
    except:
        print("Errore imprevisto!")