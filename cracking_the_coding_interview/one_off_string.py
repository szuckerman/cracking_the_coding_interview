"""Question 1.5"""


def remove_letter_from_string(string1, i):
    return string1[:i] + string1[i + 1 :]


def one_off_by_removal(string1, string2):
    for i in range(len(string1)):
        if remove_letter_from_string(string1, i) == string2:
            return True
    return False


def one_off_by_addition(string1, string2):
    for i in range(len(string2)):
        if remove_letter_from_string(string2, i) == string1:
            return True
    return False


def one_off_switch(string1, string2):
    number_of_different_characters = sum(
        1 for i, j in zip(string1, string2) if ord(i) - ord(j) != 0
    )

    if number_of_different_characters > 1:
        return False
    return True


def one_off_string(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False

    if one_off_by_removal(string1, string2):
        return True

    elif one_off_by_addition(string1, string2):
        return True

    elif one_off_switch(string1, string2):
        return True

    return False


def one_off_string_deque(string1, string2):
    from collections import deque

    d1 = deque()
    d2 = deque()

    string_iter1 = iter(string1)
    string_iter2 = iter(string2)

    letter1 = ""
    letter2 = ""

    while letter1 != "ITERATOR_DONE" and letter2 != "ITERATOR_DONE":
        try:
            letter1 = next(string_iter1, "ITERATOR_DONE")
        except StopIteration:
            letter1 = ""

        try:
            letter2 = next(string_iter2, "ITERATOR_DONE")
        except StopIteration:
            letter2 = ""

        d1.append(letter1)
        d2.append(letter2)

        if d1[-1] == d2[-1]:
            print(d1.pop())
            print(d2.pop())

    if len(d1) > 1:
        return False
