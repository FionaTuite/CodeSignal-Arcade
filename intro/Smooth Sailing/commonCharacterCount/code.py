from collections import Counter
def commonCharacterCount(s1, s2):
    common_letters = Counter(s1) & Counter(s2)  # => {'a': 2, 'c': 1}
    return (sum(common_letters.values()))
