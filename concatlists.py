"""Given two lists, concatenate the second list at the end of the first.

For example, given ``[1, 2]`` and ``[3, 4]``::

    >>> concat_lists([1, 2], [3, 4])
    [1, 2, 3, 4]

It should work if either list is empty::

    >>> concat_lists([], [1, 2])
    [1, 2]

    >>> concat_lists([1, 2], [])
    [1, 2]

    >>> concat_lists([], [])
    []
"""


def concat_lists(list1, list2):
    """Combine lists."""
   

    if list1 == [] and list2 != []:
        # if list 1 = []  but list two is [1,2] return [1,2]
       return list2
    elif list2 == [] and list1 != []:
        # if list 1 [1,2] and list2 = [], return [1,2]
        return list1
    elif list1 == [] and list2 == []:
        return []
    else:
        for item in list2:
            # if list 2 is [1,2] and for list 1 we have [8,9]
            list1.append(item)
            # list1 now [8,9,1,2]
        return list1

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO YOU!\n")
