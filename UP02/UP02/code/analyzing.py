import math
import pandas as pd


def dynamic_series_calculations(years, values):
    n = len(years)

    # вычисляем значения, которые должны быть выведены в нескольких строках
    calculations = {
        'Δy<sub>бi</sub>': [None] * n,
        'Δy<sub>цi</sub>': [0] * n,
        'T<sub>Пбi</sub>': [None] * n,
        'T<sub>Пцi</sub>': [0] * n,
        'T<sub>Рбi</sub>': [None] * n,
        'T<sub>Рцi</sub>': [0] * n,
    }

    for i in range(1, n):
        calculations['Δy<sub>бi</sub>'][i] = values[i] - values[0]
        calculations['Δy<sub>цi</sub>'][i] = values[i] - values[i - 1]
        calculations['T<sub>Пбi</sub>'][i] = (values[i] - values[0]) / values[0] * 100
        calculations['T<sub>Пцi</sub>'][i] = (values[i] - values[i - 1]) / values[i - 1] * 100
        calculations['T<sub>Рбi</sub>'][i] = values[i] / values[0]
        calculations['T<sub>Рцi</sub>'][i] = values[i] / values[i - 1]

    growth_factor_chain_prod = math.prod(calculations['T<sub>Рцi</sub>'][1:])
    growth_factor_chain_root_n = growth_factor_chain_prod ** (1 / n)
    # вычисляем значения, которые должны быть выведены в одной строке
    averages = {
        'ȳ': sum(values) / n,
        'Δȳ': (values[n - 1] - values[0]) / (n - 1),
        'T': growth_factor_chain_root_n
    }

    # округляем значения в словарях calculations и averages до 4 знаков после запятой
    calculations = {k: [round(v, 4) if v is not None else None for v in vs] for k, vs in calculations.items()}
    averages = {k: round(v, 4) for k, v in averages.items()}

    # включить использование LaTeX в Pandas
    # plt.rcParams['text.usetex'] = True
    # plt.rcParams['text.latex.unicode'] = True

    # создаем DataFrame из значений, которые должны быть выведены в нескольких строках
    df = pd.DataFrame(calculations)

    # добавляем столбец с годами
    df.insert(0, 'year', years)

    # добавляем значения, которые должны быть выведены в одной строке, в качестве дополнительных столбцов в DataFrame

    # удаляем лишние строки
    df.loc[-1] = ['year', 'Δy<sub>бi</sub>', 'Δy<sub>цi</sub>', 'T<sub>Пбi</sub>', 'T<sub>Пцi</sub>', 'T<sub>Рбi</sub>', 'T<sub>Рцi</sub>']
    df.index = df.index + 1
    df = df.sort_index()

    return df, averages['ȳ'], averages['Δȳ'], averages['T']
