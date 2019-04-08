"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible
reconstruction, return any of them.
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
['bedbath', 'and', 'beyond'].

Level: Medium

"""

# First example
# 2 inputs:
# set - 'quick', 'brown', 'the', 'fox',
# string - "thequickbrownfox",

# 1 output
# list - ['the', 'quick', 'brown', 'fox']


# Second example
# 2 inputs
# 'bed', 'bath', 'bedbath', 'and', 'beyond'
# "bedbathandbeyond"

# 1 output
# Either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond']


def get_words(_set, _str):
    # Decontsruct the word and try matching to the set of words
    letters = list(_str)
    _lst = []
    word = ''
    for i in letters:
        word += i
        if word in _set:
            print(f'Found "{word}" ')
            _lst.append(word)
            word = ''
    # If there is no possible reconstruction, then return null.
    if not _lst:
        _lst = None
    return _lst


if __name__ == "__main__":
    result = get_words({'quick', 'brown', 'the', 'fox'}, "thequickbrownfox")
    print(result)
    result = get_words({'bed', 'bath', 'bedbath', 'and',
                        'beyond'}, "bedbathandbeyond")
    print(result)
