# Write the python program to print all prime numbers less than 1000
  

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print("Prime numbers less than 1000 are:")
for num in range(1000):
    if is_prime(num):
        print(num, end=' ')
    