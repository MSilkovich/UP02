import math

def dynamic_series_calculations(years, values):
    n = len(years)

    # вычисляем значения, которые должны быть выведены в нескольких строках
    calculations = {
        'absolute_increase_base': [None] * n,
        'absolute_increase_chain': [0] * n,
        'growth_rate_base': [None] * n,
        'growth_rate_chain': [0] * n,
        'growth_factor_base': [None] * n,
        'growth_factor_chain': [0] * n,
    }

    for i in range(1, n):
        calculations['absolute_increase_base'][i] = values[i] - values[0]
        calculations['absolute_increase_chain'][i] = values[i] - values[i-1]
        calculations['growth_rate_base'][i] = (values[i] - values[0]) / values[0] * 100
        calculations['growth_rate_chain'][i] = (values[i] - values[i-1]) / values[i-1] * 100
        calculations['growth_factor_base'][i] = values[i] / values[0]
        calculations['growth_factor_chain'][i] = values[i] / values[i-1]

    # вычисляем значения, которые должны быть выведены в одной строке
    averages = {
        'average_production_volume': sum(values) / n,
        'average_absolute_increase': (values[n-1] - values[0]) / (n-1),
        'average_growth': ((values[n-1] / values[0]) ** (1 / (n-1)) - 1) * 100,
    }

    # вычисляем произведение значений growth_factor_chain под корнем в n-степени
    if n > 1:
        growth_factor_chain_prod = math.prod(calculations['growth_factor_chain'][1:])
        growth_factor_chain_root_n = growth_factor_chain_prod ** (1/n)
    else:
        growth_factor_chain_root_n = None

    return calculations, averages, growth_factor_chain_root_n

# # вычисляем результаты
# years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
# values = [18717, 18715, 18458, 18481, 18281, 18250, 17990, 18017, 17890, 17619, 17670]
# calculations, averages, growth_factor_chain_root_n = dynamic_series_calculations(years, values)

# # создаем DataFrame из значений, которые должны быть выведены в нескольких строках
# df = pd.DataFrame(calculations)

# # добавляем столбец с годами
# df.insert(0, 'year', years)

# # добавляем значения, которые должны быть выведены в одной строке, в качестве дополнительной строки в DataFrame
# df_averages = pd.DataFrame(averages, index=[0])
# df = pd.concat([df, df_averages], ignore_index=True)

# df_growth_factor_chain_root_n = pd.DataFrame({'growth_factor_chain_root_n': [growth_factor_chain_root_n]}, index=[0])
# df = pd.concat([df, df_growth_factor_chain_root_n], ignore_index=True)

# df = df.round(2)
# print(df.to_string(index=False))


# # сохраняем DataFrame в виде HTML-таблицы в файл table.html
# with open('table.html', 'w') as f:
#     f.write('<table id="analyze-table">\n')
#     f.write('<tr>\n')
#     f.write('<th>Δy<sub>бi</sub></th>\n')
#     f.write('<th>Δy<sub>цi</sub></th>\n')
#     f.write('<th>T<sub>Пбi</sub></th>\n')
#     f.write('<th>T<sub>Пцi</sub></th>\n')
#     f.write('<th>T<sub>Пцi</sub></th>\n')
#     f.write('<th>T<sub>Пцi</sub></th>\n')
#     f.write('<th>\n')
#     f.write('<div class="bottom">\n')
#     f.write('    y\n')
#     f.write('</div>\n')
#     f.write('</th>\n')
#     f.write('<th>\n')
#     f.write('<div class="bottom">\n')
#     f.write('    Δy\n')
#     f.write('</div>\n')
#     f.write('</th>\n')
#     f.write('<th>\n')
#     f.write('<div class="bottom">\n')
#     f.write('    Т<sub>р</sub>\n')
#     f.write('</div>\n')
#     f.write('</th>\n')
#     f.write('</tr>\n')
#     f.write(df.to_html(index=False, header=False))[1:-1])  # удаляем первую и последнюю строки, которые содержат теги <table> и </table>
#     f.write('\n</table>')