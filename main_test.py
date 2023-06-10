import main
import io
import sys
import re
import math
import types


def test_main_1():

    r1 = main.Rectangle(10, 20)
    r2 = main.Rectangle(100, 200)
    print(r1)
    print(r2)

    assert r1.width == 10
    assert r1.height == 20
    r1._width = 99
    r1._height = 99
    assert callable(r1.__str__) == True, 'Fucntion Check __str__()'
    print(r1.__str__())
    assert r1.width == 99
    assert r1.height == 99


def test_main_2():

    r1 = main.Rectangle(10, 20)
    r2 = main.Rectangle(100, 200)
    print(r1)
    print(r2)

    assert callable(r1.__lt__) == True, 'Fucntion Check __lt__()'
    assert callable(r1.__gt__) == True, 'Fucntion Check __gt__()'
    assert (r1 < r2) == True
    assert (r1 > r2) == False
