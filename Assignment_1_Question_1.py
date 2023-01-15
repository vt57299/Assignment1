# Write a Python Program to get the Fibonacci series between range 0 to 50.

num1 = -1
num2 = 1
print("Fibonacci series between 0 to 50 : ")
for i in range(51):
    fib_num = num1 + num2
    num1 = num2
    num2 = fib_num
    if fib_num < 51:
        print(fib_num, end =" ")