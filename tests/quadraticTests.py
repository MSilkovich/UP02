from genericpath import samefile
import unittest
import numpy as np

# from UP02.UP02.code.comparations import RegressionMetrics
from quadratic import Quadratic

x = [[1.0, 2.0, 3.0, 4.0, 5.0], 
     [83, 71, 64, 69, 69, 64, 68, 59, 81, 91, 57, 65, 58, 62], 
     [5, 10, 25, 50, 75, 100, 150, 250, 400],
     [-10, -9, -8, -7, -6, -5]]
y = [[2.0, 3.0, 5.0, 7.0, 11.0],
     [183, 168, 171, 178, 176, 172, 165, 158, 183, 182, 163, 175, 164, 175], 
     [1, 2, 3.5, 5, 8, 10, 12.5, 13, 20],
     [-20, -18, -16, -18, -20, -18]]

class TestQuadraticRegression(unittest.TestCase):

    def test_init(self):
        for i in range(len(x)):
            quad = Quadratic(x[i], y[i])
            self.assertTrue(np.array_equal(quad.x, np.array(x[i])))
            self.assertTrue(np.array_equal(quad.y, np.array(y[i])))
        
    def test_coefficient_a(self):
        excepted_a = [0.4286, -0.0168, -0.0001, -0.2857]
        for i in range(len(x)):
                quad = Quadratic(x[i], y[i])
                a, _, _, _ = quad.getCoefs()
                self.assertEqual(a, excepted_a[i])
                
    def test_coefficient_b(self):
        excepted_b = [-0.3714, 3.0867, 0.0776, -4.2286]
        for i in range(len(x)):
                quad = Quadratic(x[i], y[i])
                _, b, _, _ = quad.getCoefs()
                self.assertEqual(b, excepted_b[i])
                
    def test_coefficient_c(self):
        excepted_c = [2.0, 41.3745, 1.6178, -33.1429]
        for i in range(len(x)):
                quad = Quadratic(x[i], y[i])
                _, _, c, _ = quad.getCoefs()
                self.assertEqual(c, excepted_c[i])
                
    def test_coefficient_R(self):
        excepted_R = [0.9955, 0.6665, 0.9543, 0.2739]
        for i in range(len(x)):
            quad = Quadratic(x[i], y[i])
            _, _, _, R = quad.getCoefs()
            self.assertEqual(R, excepted_R[i])
        
    def test_uncorrect_count(self):
        x = [[1.0, 2.0], [2.0]]
        y = [[2.0, 3.0], [3.0]]
        excepted_R = -1
        excepted_coefs = -999.9999
        for i in range(len(x)):
            quad = Quadratic(x[i], y[i])
            a, b, c, R = quad.getCoefs()
            self.assertEqual(a, excepted_coefs)
            self.assertEqual(b, excepted_coefs)
            self.assertEqual(c, excepted_coefs)
            self.assertEqual(R, excepted_R)
            
    def test_uncorrect_data_letters(self):
        x = [['a', 'b', 'c', 'r']]
        y = [['a', 'b', 'c', 'r']]
        excepted_R = -1
        excepted_coefs = -999.9999
        for i in range(len(x)):
            quad = Quadratic(x[i], y[i])
            a, b, c, R = quad.getCoefs()
            self.assertEqual(a, excepted_coefs)
            self.assertEqual(b, excepted_coefs)
            self.assertEqual(c, excepted_coefs)
            self.assertEqual(R, excepted_R)


if __name__ == '__main__':
     unittest.main()

