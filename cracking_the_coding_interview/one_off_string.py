'''Question 1.5'''


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
    if sum(1 for i, j in zip(string1, string2) if ord(i) - ord(j) > 0) > 1:
        return False
    return True


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
