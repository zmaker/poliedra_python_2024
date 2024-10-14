while True:
    try:
        n = int(input("inserire un numero intero: "))
        assert n != 0
    except ValueError:
        print("Non è un numero")
    except AssertionError:
        print("r: oo")
    else:
        if n == 99:
            break
        r = 100/n
        print(f"r = {r}")

