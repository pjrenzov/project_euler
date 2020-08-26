import numpy as np

arr = []

for i in range(1,1000):
    if i%3==0 or i%5==0:
            arr.append(i)
            
sum = np.sum(arr)

print(sum)