import base64
from io import BytesIO
import threading
import numpy as np
import matplotlib, math

matplotlib.use('agg')

import matplotlib.pyplot as plt


class RegressionMetrics:
    """
    Класс RegressionMetrics для вычисления и сравнения показателей моделей регерессий
    """

    def __init__(self, a_linear, b_linear, a_quadratic, b_quadratic, c_quadratic, x, y):
        """
        Конструктор класса RegressionMetrics

        Parameters
        ----------
        a_linear: float
            коэффициент a для линейной регрессии

        b_linear: float
            коэффициент b для линейной регрессии
    
        a_quadratic: float
            коэффициент a для квадратичной регрессии

        b_quadratic: float
            коэффициент b для квадратичной регрессии

        c_quadratic: float
            коэффициент c для квадратичной регрессии

        x: list[float]
            массив значений x

        y: list[float]
            массив значений y
        """

        self.a_linear = a_linear
        self.b_linear = b_linear
        self.a_quadratic = a_quadratic
        self.b_quadratic = b_quadratic
        self.c_quadratic = c_quadratic
        self.x = x
        self.y = y

    def linear_regression_metrics(self):
        """
        Метод для вычисления коэффициента детерминации линейной регрессии

        Returns
        ----------
        float 
            коэффициент детерминации (R^2) для линейной регрессии,

        float 
            коэффициент корреляции (r) для линейной регрессии
        """

        y_predicted_linear = self.a_linear * self.x + self.b_linear # спрогнозированные значения
        residuals_linear = self.y - y_predicted_linear # разность реальных и спрогнозированных
        ss_res_linear = np.sum(residuals_linear ** 2)
        ss_tot_linear = np.sum((self.y - np.mean(self.y)) ** 2)
        r_square_linear = 1 - (ss_res_linear / ss_tot_linear) # детерминация
        correlation_linear = np.corrcoef(self.x, self.y)[0, 1] # корреляция
        if abs(r_square_linear) > 1 or abs(correlation_linear) > 1:
            return 999, 999
        return round(r_square_linear, 4), round(correlation_linear, 4)

    def quadratic_regression_metrics(self):
        """
        Метод для вычисления коэффициента детерминации квадратичной регрессии
        
        Returns
        ----------
        float 
            коэффициент детерминации (R^2) для квадратичной регрессии,

        float 
            коэффициент корреляции (r) для квадратичной регрессии
        """

        y_predicted_quadratic = self.a_quadratic * self.x**2 + self.b_quadratic * self.x + self.c_quadratic # спрогнозированные значения
        residuals_quadratic = self.y - y_predicted_quadratic # разность реальных и спрогнозированных
        ss_res_quadratic = np.sum(residuals_quadratic ** 2) # квадрат разностей
        ss_tot_quadratic = np.sum((self.y - np.mean(self.y)) ** 2) # квадрат разностей
        r_square_quadratic = 1 - (ss_res_quadratic / ss_tot_quadratic) # детерминация
        correlation_quadratic = math.sqrt(abs(r_square_quadratic)) # корреляция
        if abs(r_square_quadratic) > 1 or abs(correlation_quadratic) > 1:
            return 999, 999
        return round(r_square_quadratic, 4), round(correlation_quadratic, 4)
    
    def get_chart(self):
        """
        Метод для вычисления коэффициента детерминации квадратичной регрессии
        
        Returns
        ----------
        str 
            base64 закодированная картинка графика
        """

        # Линейная регрессия
        linear_regression = self.a_linear * self.x + self.b_linear

        # Квадратичная регрессия
        quadratic_regression = self.a_quadratic * self.x**2 + self.b_quadratic * self.x + self.c_quadratic

        lock = threading.Lock()
        
        # Построение графиков
        with lock:
            plt.figure(figsize=(8, 6))
            plt.scatter(self.x, self.y, color='blue', label='Данные')
            plt.plot(self.x, linear_regression, color='red', label='Линейная регрессия')
            plt.plot(self.x, quadratic_regression, color='green', label='Квадратичная регрессия')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.legend()
            plt.title('Графики линейной и квадратичной регрессии')
            plt.grid(True)
    
            plt.tight_layout()
    
            img = BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            
            plot_url = base64.b64encode(img.getvalue()).decode()
            plt.close()
            
            return plot_url
    