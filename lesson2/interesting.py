def find_primes(start, end):
    primes = set(range(start, end))
    k = 2

    while k < end:
        for number in set(primes) - set([k]):
            if (number % k) == 0:
                primes.remove(number)

        k += 1

    return primes


def sort_list(list1):
    list2 = list(list1)
    return sorted(list2)
