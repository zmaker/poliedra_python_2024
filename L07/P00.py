a = 10

def f1():
    a = 20
    print("a in f1: ", a)

print("1. a: ", a)
f1()
print("2. a: ", a)

def f2():
    global a
    a = 20
    print("a in f2: ", a)

print("3. a: ", a)
f2()
print("4. a: ", a)

l1 = [1,2,3]

def f3(param):
    param[0] = 99

print(l1)
f3(l1)
print(l1)

