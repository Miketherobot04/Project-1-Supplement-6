def solve_cramers_rule(coeff_matrix, constants):
    """
    Solve a system of linear equations using Cramer's rule.

    Args:
        coeff_matrix (2D array): Coefficient matrix of the system.
        constants (1D array): Constant terms.

    Returns:
        list: Solution of the variables.
    """
    import numpy as np
    det_main = np.linalg.det(coeff_matrix)
    if det_main == 0:
        raise ValueError("The system has no unique solution.")
    
    solutions = []
    for i in range(coeff_matrix.shape[1]):
        temp_matrix = coeff_matrix.copy()
        temp_matrix[:, i] = constants
        solutions.append(np.linalg.det(temp_matrix) / det_main)
    
    return solutions