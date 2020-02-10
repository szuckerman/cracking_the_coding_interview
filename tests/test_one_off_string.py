import pytest
from cracking_the_coding_interview import one_off_string as oos


def test_example1():
    string1 = "pale"
    string2 = "ple"
    assert oos.one_off_string(string1, string2) == True


def test_example2():
    string1 = "pales"
    string2 = "pale"
    assert oos.one_off_string(string1, string2) == True


def test_example3():
    string1 = "pale"
    string2 = "bale"
    assert oos.one_off_string(string1, string2) == True


def test_example4():
    string1 = "pale"
    string2 = "bake"
    assert oos.one_off_string(string1, string2) == False


def test_example5():
    string1 = "palep"
    string2 = "pleap"
    assert oos.one_off_string(string1, string2) == False


def test_example6():
    string1 = "palep"
    string2 = "palepp"
    assert oos.one_off_string(string1, string2) == True


def test_example7():
    string1 = "palep"
    string2 = "paleppp"
    assert oos.one_off_string(string1, string2) == False


def test_example8():
    string1 = "palep"
    string2 = "sales"
    assert oos.one_off_string(string1, string2) == False
