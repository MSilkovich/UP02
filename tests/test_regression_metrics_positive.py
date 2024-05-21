import unittest
from parameterized import parameterized
import numpy as np

# python -m unittest -v tests\test_regression_metrics_positive.py

from UP02.UP02 import RegressionMetrics

class TestRegressionMetricsLinearPositive(unittest.TestCase):

    @parameterized.expand([
            # нормальные данные, правильные значения параметров
            (RegressionMetrics(124.2, -239.4, None, None, None, np.array([1, 2, 3, 4, 5]), np.array([2, 4, 10, 50, 600])), 
                0.5631, 0.7504, 
                None, None),

            # расходящиеся данные, правильные коэффиценты
            (RegressionMetrics(-100, 180, None, None, None, np.array([1, 2, 3, 4, 5]), np.array([-200, 300, -500, 700, -900])), 
                0.0622, -0.2494,
                None, None),
                            
            # минимальное количество точек
            (RegressionMetrics(-150, 166.6667, None, None, None, np.array([1, 2, 3]), np.array([-200, 300, -500])), 
                0.1378, -0.3712, 
                None, None)
        ])
    def test_linear_regression_metrics(self, model: RegressionMetrics, expected_r_lr: float, expected_corr_lr: float, expected_r_qu: float, expected_corr_qu: float):
        # Проверяем корректность вычисления коэффициентов детерминации и корреляции для линейной и квадратичной регрессии
        r_square_linear, correlation_linear = model.linear_regression_metrics()
        self.assertAlmostEqual(r_square_linear, expected_r_lr, delta=0.001)  
        self.assertAlmostEqual(correlation_linear, expected_corr_lr, delta=0.001) 
    

    @parameterized.expand([
        # нормальные данные, правильные значения параметров
        (RegressionMetrics(None, None, 80.714286, -360.085714, 325.6, np.array([1, 2, 3, 4, 5]), np.array([2, 4, 10, 50, 600])), 
            None, None,
            0.8962, 0.9467),

        # расходящиеся данные, правильные коэффиценты
        (RegressionMetrics(None, None, -157.1429, 842.8571, -920, np.array([1, 2, 3, 4, 5]), np.array([-200, 300, -500, 700, -900])), 
            None, None,
            0.2772, 0.5265),
                        
        # минимальное количество точек
        (RegressionMetrics(None, None, -650.0, 2450.0, -2000.0, np.array([1, 2, 3]), np.array([-200, 300, -500])), 
            None, None,
            1.0, 1.0)
        ])
    def test_quadratic_regression_metrics(self, model: RegressionMetrics, expected_r_lr: float, expected_corr_lr: float, expected_r_qu: float, expected_corr_qu: float):
        # Проверяем корректность вычисления коэффициентов детерминации и корреляции для линейной и квадратичной регрессии
        r_square_quadratic, correlation_quadratic = model.quadratic_regression_metrics()
        self.assertAlmostEqual(r_square_quadratic, expected_r_qu, delta=0.001)  
        self.assertAlmostEqual(correlation_quadratic, expected_corr_qu, delta=0.001) 


if __name__ == '__main__':
    unittest.main()