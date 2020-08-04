"""Return index of largest num in sorted list that is smaller than given num.

For example:

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
    2

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
    4

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
    1

Never find xnumber --- it's not smaller than itself!

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
    1

If no such number exists, return None:

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
    True

"""


def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number."""
    num_return_list = []

    for num in nums:
        if num < xnumber:
            num_return_list.append(num)
    if num_return_list == []:
        return None
    else:
        # print(num_return_list)
        num_return_index = len(num_return_list)-1
        # print(num_return_index)
        return num_return_index
    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASSED. YOU ARE THE MAXIMUM!\n")

