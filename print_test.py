# factorial

# def factorial(num):
#     f = 1
#     while num > 1:
#         f *= num
#         num -= 1
#     return f

def factorial(num):
    f = 1
    for v in range(2, num + 1):
        f *= v
    return f


def main():
    num = int(input("Input your number > 0: "))
    fact = factorial(num)
    print(f"The factorial of a number {num} is [{fact}]")


main()

print(type(5))