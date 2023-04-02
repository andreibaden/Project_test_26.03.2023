def count_iteration(num):
    count = 0
    while num != 0:
        num //= 2
        count += 1

    return count


def main():
    num = int(input("Input your number > 0: "))
    count = count_iteration(num)
    print(count)


main()
