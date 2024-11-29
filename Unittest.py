import unittest
import numpy as np
from your_module import normal_distribution_array, solve_cramers_rule, integer_array_with_indices

class TestFunctions(unittest.TestCase):
    def test_normal_distribution_array(self):
        arr = normal_distribution_array((2, 3), 0, 1)
        self.assertEqual(arr.shape, (2, 3))
        self.assertAlmostEqual(np.mean(arr), 0, delta=0.5)
        self.assertAlmostEqual(np.std(arr), 1, delta=0.5)

    def test_solve_cramers_rule(self):
        coeff_matrix = np.array([[2, -1], [1, 1]])
        constants = np.array([1, 4])
        solution = solve_cramers_rule(coeff_matrix, constants)
        self.assertAlmostEqual(solution[0], 2)
        self.assertAlmostEqual(solution[1], 3)

    def test_integer_array_with_indices(self):
        array, even_indices, odd_indices = integer_array_with_indices((3, 3))
        for idx in even_indices:
            self.assertEqual(array[idx] % 2, 0)
        for idx in odd_indices:
            self.assertNotEqual(array[idx] % 2, 0)