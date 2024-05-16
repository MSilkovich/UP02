# Импортируем необходимые библиотеки
import numpy as np
import io
import base64
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Получаем данные из другого модуля
# X - признаки, y - целевая переменная
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([1, 3, 7, 13, 21, 31, 43, 57, 73, 91])

# подсчеты
def calculations():
    # Вычисляем линейную регрессию
    lr_model = LinearRegression()
    lr_model.fit(X, y)
    lr_pred = lr_model.predict(X)

    # Вычисляем квадратичную регрессию
    X_poly = np.c_[X, np.power(X, 2)]
    poly_model = LinearRegression()
    poly_model.fit(X_poly, y)
    poly_pred = poly_model.predict(X_poly)

    # Вычисляем коэффициенты корреляции и детерминации
    lr_corr = np.corrcoef(y, lr_pred)[0, 1]
    lr_determ = r2_score(y, lr_pred)

    poly_corr = np.corrcoef(y, poly_pred)[0, 1]
    poly_determ = r2_score(y, poly_pred)

    # Сравниваем коэффициенты детерминации
    res_str = ""
    if lr_determ > poly_determ:
        res_str = "Линейная регрессия лучше аппроксимирует исходные данные"
    elif lr_determ < poly_determ:
        res_str = "Квадратичная регрессия лучше аппроксимирует исходные данные"
    else:
        res_str = "Линейная и квадратичная регрессия одинаково хорошо аппроксимируют исходные данные"
    return res_str, lr_corr, lr_determ, lr_pred, poly_corr, poly_determ, poly_pred


# Визуализируем исходные данные и линии регрессии
def create_chart():
    res_str, lr_corr, lr_determ, lr_pred, poly_corr, poly_determ, poly_pred = calculations()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Сравнение')
    plt.scatter(X, y, color='blue')
    plt.plot(X, lr_pred, color='red', label='Линеная регрессия')
    plt.plot(X, poly_pred, color='green', label='Квадратичная регрессия')
    plt.legend()

    # сохраняем график в буфер
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # кодируем буфер в base64
    image_data = base64.b64encode(buf.read()).decode()

    # закрываем текущий график
    plt.close()

    return image_data
