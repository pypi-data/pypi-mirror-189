from typing import List, Union

def harmonic_mean(numbers: List[Union[float, int]]) -> float:
    """
    Calculates the harmonic mean of a list of floating-point numbers.

    Parameters:
    numbers (List[Union[float, int]]): A list of floating-point numbers to calculate the harmonic mean of.

    Restrictions:
    numbers list should contain only numeric values(int or float)
    numbers list should contain only positive numbers (greater than zero)
    numbers list should not be empty

    Returns:
    float: The harmonic mean of the given numbers.
    """

    # The error handling below results in slower execution.
    if not numbers:
        raise ValueError("Numbers list must not be empty.")
    if any(isinstance(i, (int, float)) == False for i in numbers):
        raise TypeError("Numbers list must contain only numeric values.")
    if any(i <= 0 for i in numbers):
        raise ValueError("Numbers list must contain only strictly positive numbers.")

    n = len(numbers)
    return n / sum(1/x for x in numbers)

