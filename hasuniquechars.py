"""Does word contains unique set of characters?

For example::

    >>> has_unique_chars("Monday")
    True

    >>> has_unique_chars("Moonday")
    False

    >>> has_unique_chars("")
    True

Uppercase and lowercase letters should be considered separately::

    >>> has_unique_chars("Bob")
    True
"""


def has_unique_chars(word):
    """Does word contains unique set of characters?"""
    newList= []
    if word == []:
        return True
    else:
       word = list(word)
       for letters in word:
            if letters not in newList:
               newList.append(letters)
            else:
                return False
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AWESOME!\n")
