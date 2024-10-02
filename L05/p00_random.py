import random
from datetime import datetime

print(datetime.now().timestamp())

random.seed(datetime.now().timestamp())

for i in range(10):
    n = random.randint(0, 100)
    print(n)