"""Return the largest integer in a list.

Given a list of integers, return the largest. Do not use the built in 'max' method.

For example::

    >>> max_num([1, 3, 2, 4, 7, 2])
    7

    >>> max_num([5, 5, 5])
    5

    >>> max_num([10])
    10

    >>> max_num([-1, -2, -3])
    -1

    >>> max_num([-10, 0])
    0

"""


def max_num(num_list):
    """Returns largest integer from given list"""
    if len(num_list) == 0:
        return 0
    elif len(num_list)== 1:
        return num_list[0]
    else:
        num_list = sorted(num_list)
        num_list = num_list[::-1]
        for i in range(len(num_list)-1):
            if num_list[i+1] > num_list[i]+1:
                num_list.pop(i)
            elif num_list[i] == num_list[i+1]:
                num_list.pop(i)
            else:
                num_list.pop(i+1)
            return num_list[0]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO YOU!\n")
