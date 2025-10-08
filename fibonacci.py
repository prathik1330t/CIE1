n = int(input("Enter the number of Fibonacci terms to sum: "))
a=0
b=1
sum = 0
i = 0
while i < n:
    sum = sum + a 
    a, b = b, a + b      
    i = i + 1             
print(f"The sum of the first {n} Fibonacci numbers is {sum}")
