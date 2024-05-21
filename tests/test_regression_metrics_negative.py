import unittest
from parameterized import parameterized
import numpy as np

# python -m unittest -v tests\test_regression_metrics_negative.py

from UP02.UP02 import RegressionMetrics

class TestRegressionMetricsLinearNegative(unittest.TestCase):

    @parameterized.expand([
            # x меньше, чем число соответствующих y
            (RegressionMetrics(124.2, -239.4, 80.714286, -360.085714, 325.6, np.array([1, 2, 3, 4]), np.array([2, 4, 10, 50, 600])), 
                None, None,
                None, None),

            # символ в массиве
            (RegressionMetrics(-100, 180, -157.1429, 842.8571, -920, np.array(["d", 2, 3, 4, 5]), np.array([-200, 300, -500, 700, -900])), 
                None, None,
                None, None),
                            
            # x больше, чем число соответствующих y
            (RegressionMetrics(-150, 166.6667, -650.0, 2450.0, -2000.0, np.array([1, 2, 3, 4, 5]), np.array([-200, 300, -500])), 
                None, None,
                None, None),
                            
            # недостаточно точек
            (RegressionMetrics(-150, 166.6667, -650.0, 2450.0, -2000.0, np.array([1, 2]), np.array([-200, 300])), 
                None, None,
                None, None),
        ])
    
    def test_linear_regression_metrics(self, model: RegressionMetrics, expected_r_lr: float, expected_corr_lr: float, expected_r_qu: float, expected_corr_qu: float):
        # Проверяем НЕкорректные случаи вычисления коэффициентов детерминации и корреляции для линейной регрессии
        with self.assertRaises(Exception):
            r_square_linear, correlation_linear = model.linear_regression_metrics()
            self.assertAlmostEqual(r_square_linear, expected_r_lr, delta=0.001)  
            self.assertAlmostEqual(correlation_linear, expected_corr_lr, delta=0.001) 

            r_square_quadratic, correlation_quadratic = model.quadratic_regression_metrics()
            self.assertAlmostEqual(r_square_quadratic, expected_r_qu, delta=0.001)  
            self.assertAlmostEqual(correlation_quadratic, expected_corr_qu, delta=0.001) 


if __name__ == '__main__':
    unittest.main()