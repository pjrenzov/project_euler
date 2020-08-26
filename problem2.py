sum = 2

fib = 2
fib_prev = 1

while fib < 4000000:
    fib, fib_prev = fib+fib_prev, fib
    
    if fib%2==0:
        sum+=fib
        
print(sum)