"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""

    if not (len(w1) + 1 == len(w2) or len(w1) - 1 == len(w2) or len(w1) == len(w2)):
        return False

    p1 = p2 = 0
    extra_or_wrong_letter = 0

    if len(w1) + 1 == len(w2):
        while p1 < len(w1) and p2 < len(w2):
            if w1[p1] == w2[p2]:
                p1 += 1
            else:
                extra_or_wrong_letter += 1
            p2 += 1

    elif len(w1) - 1 == len(w2):
        while p1 < len(w1) and p2 < len(w2):
            if w1[p1] == w2[p2]:
                p2 += 1
            else:
                extra_or_wrong_letter += 1
            p1 +=1

    elif len(w1) == len(w2):
        while p1 < len(w1) and p2 < len(w2):
            if w1[p1] != w2[p2]:
                extra_or_wrong_letter += 1
            p1 += 1
            p2 += 1

    if extra_or_wrong_letter > 1:
        return False

    return True



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
