# def fact(n):
#     mul = 1
#     for i in range(1,n+1):
#         mul *= i
#     return mul
#
# print(fact(5))


# Writing to a file
# with open('example.txt', 'w') as file:
#     file.write("Hello, this is a simple file handling example.\n")
#     file.write("This is the second line.")

# Reading from a file
# with open('example.txt', 'r') as file:
#     # line1 = file.readline()
#     # print(line1.strip())
#     for line in file:
#         print(line.strip())
# def fibo(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         temp = a + b
#         a = b
#         b = temp
#
# # Example usage
# n = 10  # Number of Fibonacci numbers to generate
# fibo(n)

a = [2,3,4,5]
a.append('3',5)
print(a)