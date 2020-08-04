"""Translate phrase to "leet-speak".

For example::

    >>> translate_leet("Hi Balloonicorn")
    'Hi B@1100nic0rn'

    >>> translate_leet("Hackbright is the Shizzle")
    'H@ckbrigh7 i5 7h3 5hizz13'

"""


def translate_leet(phrase):
    """Translates input into "leet-speak"."""
    leet_dict = {'a':'@', 'e': '3', 'o': '0','t':'7','s':'5', 'S': '5', 'l':'1'}
    phrase = list(phrase)
    new_phrase = []
    for letters in phrase:
        if letters in leet_dict.keys():
            new_phrase.append(leet_dict[letters])
        else:
            new_phrase.append(letters)
    return ''.join(new_phrase)

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AE3S0M3!\n")
