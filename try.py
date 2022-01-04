def multiply(a, b):
    """
    Takes two values and returns the product
    :param a:
    :param b:
    :return: product
    """
    res = a * b
    return res


def add(a, b, c):
    """
        Takes two values and returns the addition
        :param c:
        :param a:
        :param b:
        :return: addition
        """
    res = a + b + c
    return res


# calculate (2.5*3) +4
print(add(multiply(2.5, 3), 4, 0))

# calculate (1*2) +3
print(add(multiply(1, 2), 3, 0))
print(__name__)
