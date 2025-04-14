#Write a Python program to count number of even numbers and odd numbers in a given set of n numbers.


arr = {1,2,3,4,5,6,7,8,10}
n=len(arr)
even=0
odd=0
for i in range(n):
    if((i%2) == 0):
        even = even+1
    else:
        odd=odd+1
print(even)
print(odd)