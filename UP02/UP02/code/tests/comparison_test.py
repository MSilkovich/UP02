import unittest
import numpy as np

from UP02.UP02.code.comparations import RegressionMetrics

class Test_RegressionMetrics_tests(unittest.TestCase):

    def setUp(self):
        # Подготовка данных для тестов
        self.x = np.array([1, 2, 3, 4, 5])
        self.y = np.array([2, 3, 4, 5, 6])

        # Коэффициенты для линейной регрессии
        self.a_linear = 0.5
        self.b_linear = 1.5

        # Коэффициенты для квадратичной регрессии
        self.a_quadratic = 0.5
        self.b_quadratic = 1.5
        self.c_quadratic = 0.5

        self.regression_metrics = RegressionMetrics(self.a_linear, self.b_linear,
                                                    self.a_quadratic, self.b_quadratic,
                                                    self.c_quadratic, self.x, self.y)

    def test_linear_regression_metrics(self):
        # Проверяем корректность вычисления коэффициентов детерминации и корреляции для линейной регрессии
        r_square_linear, correlation_linear = self.regression_metrics.linear_regression_metrics()
        self.assertAlmostEqual(r_square_linear, 0.0)  # Замените на ожидаемое значение
        self.assertAlmostEqual(correlation_linear, 0.0)  # Замените на ожидаемое значение

    def test_quadratic_regression_metrics(self):
        # Проверяем корректность вычисления коэффициентов детерминации и корреляции для квадратичной регрессии
        r_square_quadratic, correlation_quadratic = self.regression_metrics.quadratic_regression_metrics()
        self.assertAlmostEqual(r_square_quadratic, 0.0)  # Замените на ожидаемое значение
        self.assertAlmostEqual(correlation_quadratic, 0.0)  # Замените на ожидаемое значение

    def test_get_chart(self):
        # Проверяем, что метод get_chart возвращает строку
        plot_data = self.regression_metrics.get_chart()
        self.assertIsInstance(plot_data, str)

        # Проверяем, что возвращаемая строка содержит "base64", что указывает на base64 закодированную картинку
        self.assertIn("base64", plot_data)


unittest.main()