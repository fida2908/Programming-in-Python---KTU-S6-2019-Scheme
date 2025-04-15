# Write a python program to generate the following type of pattern for the given N rows.
# 1
# 1 2
# 1 2 3
# 1 2 3 4.





n = int(input('Enter the number of ip: '))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()