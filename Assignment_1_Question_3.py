# Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_nos = 0
odd_nos = 0
for i in numbers:
    if i % 2 == 0:
        even_nos += 1
    else:
        odd_nos += 1

print("Total even numbers are : ", even_nos)
print("Total odd NUmbers are : ", odd_nos)