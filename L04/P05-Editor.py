testo = ""

print("digita q per terminare")
while (True):
    line = input("> ")
    if line == 'q':
        break;
    testo += line + "\n"
    print(testo)
