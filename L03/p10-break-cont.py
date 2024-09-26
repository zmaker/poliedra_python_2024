for i in range(10):
    print(i, end=' ')
    if (i == 5):
        break;

print("\n")

for i in range(10):
    if (i == 5):
        continue;
    print(i, end=' ')

print("\n")
count = 0
while (count < 10):
    if (count == 5):
        break;
    print(count, end = ' ')
    count += 1

print("\n")
count = 0
while (count < 10):
    count += 1
    if (count == 5):
        continue;
    print(count, end = ' ')

