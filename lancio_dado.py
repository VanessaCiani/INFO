import random

dado = 0

for i in range(10000):
    dado = dado + random.randint (1, 6)
    
print("Il numero medio delle estrazioni del dado è:", dado /10000)
