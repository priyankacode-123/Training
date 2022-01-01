def multiply(a, b):
    """
    Takes two values and returns the product
    :param a:
    :param b:
    :return: product
    """
    res = a * b
    return res


def add(a, b):
    """
        Takes two values and returns the addition
        :param a:
        :param b:
        :return: addition
        """
    res = a + b
    return res


# calculate (2.5*3) +4
print(add(multiply(2.5, 3), 4))

# calculate (1*2) +3
print(add(multiply(1, 2), 3))
print(__name__)
