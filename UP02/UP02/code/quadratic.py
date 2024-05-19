from scipy.optimize import curve_fit
import numpy as np
from scipy.stats import pearsonr


class Quadratic:
    """����� ��� �������� ������������ ������������ ���������."""

    def __init__(self, x, y):
        """x - �������� x
           y - ��������������� �������� y
        """
        self.x = np.array(x)
        self.y = np.array(y)
        popt, _ = curve_fit(self.quadratic_func, self.x, self.y)
        self.a, self.b, self.c = popt
        quadratic_coeff = np.polyfit(x, y, 2)
        y_pred = np.polyval(quadratic_coeff, x)
        correlation_coefficient, _ = pearsonr(y, y_pred)
        self.R = correlation_coefficient ** 2

    def quadratic_func(self, x, a, b, c):
        return a * x ** 2 + b * x + c

    def getCoefs(self):
        """��������� ������������� a0, a1, a2 � R2"""
        return round(self.a, 4), round(self.b, 4), round(self.c, 4), round(self.R, 4)

