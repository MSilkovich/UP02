import numpy as np


# Создаем исходные данные
# x = np.array([0, 1, 2, 3, 4, 5])
# y = np.array([1, 3, 2, 5, 7, 8])

def linear_approximation(x, y):
    # Фитируем многочлен первой степени (линейная регрессия)
    p = np.polyfit(x, y, 1)

    # Получаем коэффициенты многочлена
    a0, a1 = p

    # Рассчитываем коэффициент детерминации R2
    # y_fit = np.polyval(p, x)
    # y_mean = np.mean(y)
    # ss_tot = np.sum((y - y_mean)**2)
    # ss_res = np.sum((y - y_fit)**2)
    # r_squared = 1 - ss_res / ss_tot
    
    return round(a0, 4), round(a1, 4)