import unittest
import numpy as np

# python -m unittest -v tests\comparison_test.py

from UP02.UP02 import RegressionMetrics

class Test_RegressionMetrics_tests(unittest.TestCase):

    def setUp(self):
        # Подготовка данных для тестов defaul конфигурация
        self.x = np.array([1, 2, 3, 4, 5])
        self.y = np.array([2, 4, 10, 50, 600])

        # Коэффициенты для линейной регрессии
        self.a_linear = 124.2
        self.b_linear = -239.4

        # Коэффициенты для квадратичной регрессии
        self.a_quadratic = 80.714286
        self.b_quadratic = -360.085714
        self.c_quadratic = 325.6

        self.regression_metrics = RegressionMetrics(self.a_linear, self.b_linear,
                                                    self.a_quadratic, self.b_quadratic,
                                                    self.c_quadratic, self.x, self.y)

    def test_linear_regression_metrics_by_default(self):
        # Проверяем корректность вычисления коэффициентов детерминации и корреляции для линейной регрессии
        r_square_linear, correlation_linear = self.regression_metrics.linear_regression_metrics()
        self.assertAlmostEqual(round(r_square_linear, 4), 0.5631, delta=0.001)  
        self.assertAlmostEqual(round(correlation_linear, 4), 0.7504, delta=0.001)  
        
    def test_linear_regression_metrics_by_high_nums(self):
        self.x = np.array([2018, 2019, 2020, 2021, 2022])
        self.y = np.array([1, 10, 30, 5, 25])
        self.a_linear = -8671.8
        self.b_linear = 4.3
        self.a_quadratic = 0
        self.b_quadratic = 0
        self.c_quadratic = 0
        self.regression_metrics = RegressionMetrics(self.a_linear, self.b_linear,
                                                    self.a_quadratic, self.b_quadratic,
                                                    self.c_quadratic, self.x, self.y)
        
        # Проверяем корректность вычисления коэффициентов детерминации и корреляции для линейной регрессии
        r_square_linear, _ = self.regression_metrics.linear_regression_metrics()
        self.assertAlmostEqual(round(r_square_linear, 4), 0.288, delta=0.001)  


if __name__ == '__main__':
    unittest.main()