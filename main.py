
class Rectangle:
    #########################################
    # Code your program here
    #########################################


def main():
    r1 = Rectangle(10, 20)
    r2 = Rectangle(100, 200)
    print(r1)
    print(r2)
    r1._width = 99
    r1._height = 99
    print(r1)

    if r1 > r2:
        print('Rectangle r1 is greater than r2')
    else:
        print('Rectangle r1 is not greater than r2')
    if r1 < r2:
        print('Rectangle r1 is less than r2')
    else:
        print('Rectangle r1 is not less than r2')


if __name__ == '__main__':
    main()
