# import numpy as np
import pandas as pd
# import re

# import scipy.stats as sts
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

# не знаю, понадобятся ли мне все библиотеки, но предвариетльно импортирую всё, что смогла найти по семинарам

# загрузим сюда наш датасет

# в ручном режиме убираю лишнюю строку с заголовками второго датасета!!!

df = pd.read_csv("C:/Users/Саша/Python_Basic/Andan_project/total_data_set.csv", error_bad_lines=False, engine ='python')
# Я не знаю, с чего начать, поэтому начнем строить графики и искать зависимости по порядку по всем модулям.
# Первый будет Диаграмма рассеяния (scatter plot)


# Для Жанра и счёта
# fig = sns.scatterplot(data=df, y="genre", x="score")
fig2 = sns.lineplot(data=df, y="genre", x="score")
# fig3 = sns.countplot(x ='genre', data = df)
# fig4 = sns.countplot(x ='score', data = df)
# Меняю формат столбца, чтобы сделать ящик с усами, так как он требует хотя бы один столбец с numeric значениями
# ser = pd.Series(df['score'])
# ser = ser.replace('score', '')
# ser = pd.to_numeric(ser)
# fig5 = sns.boxplot(data=df, y=df['genre'], x=ser)
plt.show()


# Для Года и счёта
# fig = sns.scatterplot(data=df, x="release_year", y="score")
# fig2 = sns.lineplot(data=df, y="release_year", x="score")
# fig3 = sns.countplot(x ='release_year', data = df)
# Меняю формат столбца, чтобы сделать ящик с усами
# fig4 = sns.boxplot(data=df, y=df['release_year'], x=ser)
# plt.show()


# Для Месяца и счёта
# fig = sns.scatterplot(data=df, x="release_month", y="score")
# fig2 = sns.lineplot(data=df, y="release_month", x="score")
# fig3 = sns.countplot(x ='release_month', data = df)
# Меняю формат столбца, чтобы сделать ящик с усами
# fig4 = sns.boxplot(data=df, y=df['release_month'], x=ser)
# plt.show()


# Для Платформы и счёта
# fig = sns.scatterplot(data=df, y="platform", x="score")
# fig2 = sns.lineplot(data=df, y="platform", x="score")
# fig3 = sns.countplot(x ='platform', data = df)


# ЭТО Я СПЁРЛА!!! НАДО ПЕРЕФРАЗИРОВАТЬ И СДЕЛАТЬ ВЫВОДЫ ПРО ПЛАТФОРМЫ
# platform = df.platform.value_counts().reset_index()
# platform.rename(columns={'index':'platform', 'platform':'count'}, inplace=True)
# platform.sort_values(by='count', ascending=False, inplace=True)
# plt.figure(figsize=(13,4))
# fig = platform[0:10].plot(x='platform', y='count', kind='barh', figsize=(15,6))


# Меняю формат столбца, чтобы сделать ящик с усами
# fig4 = sns.boxplot(data=df, y=df['platform'], x=ser)

# ser1 = pd.Series(df['release_year'])
# ser1 = ser1.replace('release_year', '')
# ser1 = pd.to_numeric(ser1)
# fig5 = sns.boxplot(data=df, y=df['platform'], x=ser1)

# plt.show()


# Для Жанра и платформы
# fig = sns.scatterplot(data=df, x="genre", y="platform")
# fig2 = sns.lineplot(data=df, y="genre", x="platform")
# Меняю формат столбца, чтобы сделать ящик с усами
# plt.show()


# Подведем предварительные итоги:
#
# 1) Какие удалось выявить зависимости?


# 2) Какие хочу проверять гипотезы?
#
# Я думаю, я хочу проверить,


