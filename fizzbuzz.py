"""Count from 1 to 20 in fizzbuzz fashion.

Loop from 1 to 20 (inclusive). Each through, if the iber
is evenly divisible by 3, say 'fizz'. If the iber is evenly
divisible by 5, say 'buzz'. If the iber is evenly divisible
by both 3 and 5, say 'fizzbuzz'. Otherwise, say the iber.

    >>> fizzbuzz()
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    17
    fizz
    19
    buzz
"""


def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion."""
    fizzbuzz_count = []
    for num in range(1,21):
        if num %3 == 0 and num %5 ==0:
            num = "fizzbuzz"
            fizzbuzz_count.append(num)
        elif num %3 ==0 and num %5 !=0:
            num = "fizz"
            fizzbuzz_count.append(num)
        elif num %5 ==0 and num %3 !=0:
            num = "buzz"
            fizzbuzz_count.append(num)
        else:
            num = str(num)
            fizzbuzz_count.append(num)
    for num in fizzbuzz_count:
        print(num)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. FIZZBUZZ FOR THE WIN!\n")
