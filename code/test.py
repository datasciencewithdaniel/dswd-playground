def add_function(a_variable: int, b_variable: int) -> int:
    """
    function to add two numbers

    Args:
        a_variable (int): number 1
        b_variable (int): number 2

    Returns:
        int: the added number
    """

    c_variable = a_variable + b_variable
    return c_variable


if __name__ == "__main__":
    print(add_function(3, 4))
    # print(add_function("3", 4))
