# Task 1
def squares_up_to_n(N):
    for i in range(1, N + 1):
        yield i * i

N = 10
print("Squares up to N:")
for square in squares_up_to_n(N):
    print(square)

# Task 2
def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter the value of n: "))
even_numbers_str = ",".join(str(num) for num in even_numbers(n))
print("Even numbers:")
print(even_numbers_str)

# Task 3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter the value of n: "))
print("Numbers divisible by 3 and 4:")
for num in divisible_by_3_and_4(n):
    print(num)

# Task 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("Squares from a to b:")
for square in squares(a, b):
    print(square)

# Task 5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter the value of n: "))
print("Countdown from n to 0:")
for num in countdown(n):
    print(num)
