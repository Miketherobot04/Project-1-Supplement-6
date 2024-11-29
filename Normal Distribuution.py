def normal_distribution_array(shape, mean, std_dev):
    """
    Generate an array of normally distributed numbers.

    Args:
        shape (tuple): The shape of the array.
        mean (float): The mean of the distribution.
        std_dev (float): The standard deviation of the distribution.

    Returns:
        numpy.ndarray: Array of normally distributed numbers.
    """
    import numpy as np
    return np.random.normal(loc=mean, scale=std_dev, size=shape)