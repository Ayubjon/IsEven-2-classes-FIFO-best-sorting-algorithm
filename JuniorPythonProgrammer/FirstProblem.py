# ---------------------------------------
# FIRST PROBLEM
# ---------------------------------------

# My function is faster because operations like a 'and', 'or', 'xor' work faster.
# Operation '%' uses division and subtraction and of course it's slower.
def isEven(number: int) -> bool:
    return not (number & 1)


def printIsEven(number: int):
    if isEven(number):
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")


def testIsEven():
    printIsEven(1)
    printIsEven(144)
    printIsEven(101)
    printIsEven(2051033)
    print("Enter a number to check for is it even or odd: ", end="")
    number = int(input())
    printIsEven(number)


# Hello, here I will code and test problems that
# I got like a test for Junior Python Programmer position.
if __name__ == '__main__':
    testIsEven()
