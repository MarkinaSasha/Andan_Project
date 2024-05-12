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

# Пока делала обнаружила одну ошибку... Похоже, я всё таки оставиле кое-где мультижанровость.
# Обязательно это исправлю, потому что это путает

# ВАЖНО
# Все мои графики закомментированы, потому что я прогоняла их кучу раз, и мне не нужно,
# чтобы они все постоянно активировались, когда мне нужен только один последний график

# Буду попарно проверять все признаки в надежде найти взаимосвязи. В любом случае, я буду добавлять еще признаков
# Так что это не финальный вариант
# ************************************************************************************************************
# Для Жанра и счёта

# fig = sns.scatterplot(data=df, y="genre", x="score")
# plt.show()
# закономерностей не нашла, возможно мультижанровасть попортила всё. Исправлю

# fig2 = sns.lineplot(data=df, y="genre", x="score")
# plt.show()
# если я правильно прочитала график, кажется, что оценки выше у
# однопользовательских игр (обычно жанры Хоррор, Платформер, Симуляции и тд жанры синглплэерные).
# Более низкие оценки у игр про спорт и развитие

# fig3 = sns.countplot(y ='genre', data = df)
# plt.show() # Наибольшее количество игр в жанре Экшн

# fig4 = sns.countplot(y ='score', data = df)
# plt.show()
# У подавляющего большинства оценки стоят выше 6, больше всего восьмёрок

# Меняю формат столбца, чтобы сделать ящик с усами, так как он требует хотя бы один столбец с numeric значениями
ser = pd.Series(df['score'])
ser = ser.replace('score', '')
ser = pd.to_numeric(ser)
# fig5 = sns.boxplot(data=df, y=df['genre'], x=ser)
# plt.show()
# вот этот график для меня самый важный пока что. Он структурирует все токи и показывает,
# где они концентрируются, то есть как раз примерно средняя оценка жанра. Примечательно, что экшн это и
# самый многочисленный жанр, и один и самых высокооцениваемых

# ************************************************************************************************************

# Для Года и счёта

# fig = sns.scatterplot(data=df, x="release_year", y="score")
# plt.show()
# По первому графику сложно что-то сказать.
# Как будто в последние годы стало меньше плохих оценок. Люди стали лояльнее?

# fig2 = sns.lineplot(data=df, y="release_year", x="score")
# plt.show()
# Вывод аналогичен предыдущему.

# fig3 = sns.countplot(x ='release_year', data = df)
# plt.show()
# Больше всего игры выпускалось в 2009 году. Кажется, график выглядит интересно, но пока не знаю, как его использовать

# Меняю формат столбца, чтобы сделать ящик с усами
# fig4 = sns.boxplot(data=df, y=df['release_year'], x=ser)
# plt.show()
# Вывод всё тот же. С каждым годом оценки всё выше и выше (в среднем)

# ************************************************************************************************************

# Для Месяца и счёта

# fig = sns.scatterplot(data=df, x="release_month", y="score")
# plt.show()
# 0 полезной инфы

# fig2 = sns.lineplot(data=df, y="release_month", x="score")
# plt.show()
# как будто наиболее высокие оценки выставлялись в 9-7 месяцы. Это июль-сентябрь.
# Видимо солнышко и все радостные и лояльные

# fig3 = sns.countplot(x ='release_month', data = df)
# plt.show()
# больше всего игр выходило в ноябре. Не знаю как применить


# Меняю формат столбца, чтобы сделать ящик с усами
# fig4 = sns.boxplot(data=df, y=df['release_month'], x=ser)
# plt.show()
# наиболее высокие оценки идут с 5 по 10 месяцы. Это с мая по октябрь.

# ************************************************************************************************************

# Для Платформы и счёта

# fig = sns.scatterplot(data=df, y="platform", x="score")
# plt.show()
# снова не могу ничего сказать по этому графику. Наверное я что-то делаю не так

# fig2 = sns.lineplot(data=df, y="platform", x="score")
# plt.show()
# на платформах с Meta Quest Pro до Nintendo 64 DD были замечены оценки от 10 до 7 - то есть самые предпочтительные.
# Возможно самые лучшие платформы для релиза)

# fig3 = sns.countplot(y ='platform', data = df)
# plt.show()
# Больше всего вышло игр на ПК

# Вот этот кусок пока не обработала. Я потеряла сайт, откуда взяла его, но я его обязательно найду...
# Это должна быть круговая диаграмма. Пока не знаю, пригодится она или нет
# # platform = df.platform.value_counts().reset_index()
# # platform.rename(columns={'index':'platform', 'platform':'count'}, inplace=True)
# # platform.sort_values(by='count', ascending=False, inplace=True)
# # plt.figure(figsize=(13,4))
# # fig = platform[0:10].plot(x='platform', y='count', kind='barh', figsize=(15,6))


# Меняю формат столбца, чтобы сделать ящик с усами
# fig4 = sns.boxplot(data=df, y=df['platform'], x=ser)
# plt.show()
# как будто тот же вывод, что и предыдущий

# ser1 = pd.Series(df['release_year'])
# ser1 = ser1.replace('release_year', '')
# ser1 = pd.to_numeric(ser1)
# fig5 = sns.boxplot(data=df, y=df['platform'], x=ser1)
# plt.show()
# Вот тут прикольно, что игры, на платформах которых были наибольшие оценки - это всё более старые игры
# до 2015 вроде. Учту это при проверке гипотез

# ************************************************************************************************************

# Для Жанра и платформы
# fig = sns.scatterplot(data=df, x="genre", y="platform")
# plt.show()
# Не понимаю, какие можно сделать выводы. Уберу мультижанровость и попробую еще раз

# fig2 = sns.lineplot(data=df, y="genre", x="platform")
# plt.show()
# Делаю вывод, что игры в жанре Экшн выходили на большем количестве платформ, чем другие игры.

