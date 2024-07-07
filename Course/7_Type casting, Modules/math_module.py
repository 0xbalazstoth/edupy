def add(*args: int):
    """description

    Returns:
        int: Sum of the given numbers
    """
    return sum(args)


def subtract(x: int, y: int) -> int:
    """description

    Args:
        x (int): x number
        y (int): y number

    Returns:
        int: Difference between x and y numbers
    """
    return x - y


# Akadjon ki a nullával való osztásra, ezzel demonstrálva a monkey patching-et.
def divide(x: int, y: int) -> float:
    """description

    Args:
        x (int): x number
        y (int): y number

    Returns:
        float: Quotient of x and y numbers
    """
    return x / y
