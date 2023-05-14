import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    r1 = main.Rectangle(10, 20)
    r2 = main.Rectangle(100, 200)
    print(r1)
    print(r2)
    assert r1.width == 10
    assert r1.height == 20
    r1._width = 99
    r1._height = 99
    print(r1)
    print(r2)
    assert r1.width == 99
    assert r1.height == 99

    assert (r1 < r2) == True
    assert (r1 > r2) == False

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*Elapsed'
    # regex_string += r'[\w,\W]*time'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, lines[1])
    # assert res != None
    # print(res.group())
