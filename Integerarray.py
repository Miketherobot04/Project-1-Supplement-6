def integer_array_with_indices(shape):
    """
    Generate an array of integers and separate even/odd indices.

    Args:
        shape (tuple): Shape of the array.

    Returns:
        tuple: Generated array, list of even indices, list of odd indices.
    """
    import numpy as np
    array = np.random.randint(0, 100, size=shape)
    even_indices = list(zip(*np.where(array % 2 == 0)))
    odd_indices = list(zip(*np.where(array % 2 != 0)))
    return array, even_indices, odd_indices