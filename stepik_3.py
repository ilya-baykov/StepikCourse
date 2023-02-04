def primes():
    digit = 2
    while True:
        flag = True
        while flag:
            for num in range(2, digit):
                if digit % num == 0:
                    flag = False
                    digit += 1
                    break
            if flag:
                digit += 1
                yield digit - 1


if __name__ == '__main__':
    test_1 = primes()
    print(next(test_1))
    print(next(test_1))
    print(next(test_1))
    print(next(test_1))
    print(next(test_1))
    print(next(test_1))
    print(next(test_1))
    print(next(test_1))
    print(next(test_1))
    print(next(test_1))

    # print(list(itertools.takewhile(lambda x: x <= 31, primes())))
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
