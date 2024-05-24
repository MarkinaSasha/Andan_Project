import pandas as pd
import matplotlib.pyplot as plt

with open('total_data_set.csv', 'r', encoding='utf-8') as ds:
    df = pd.read_csv(ds)

    # Начнем с описания непрерывных переменных.
    print(df.isnull().sum())
    # Пропусков нет, идем дальше

    # Посмотрим, есть ли выбросы
    fig = df.hist()
    plt.show()

    # И да и нет. По исходным признакам выбросов нет, но этот пункт я доделывала после шага 5,
    # когда я создала новые переменные. И они показали (в частности Prop_of_genre_on_platf), что выбросы есть
    # Например, на некоторых платформах значение Prop_of_genre_on_platf = 1.0
    # Это значит, что либо на этой платформе за все года выпускались игры только в одном жанре
    # Либо, что более вероятно, в моей выборке слишком мало данных об этой платформе, поэтому надо убирать строки
    # Со значением Prop_of_genre_on_platf = 1.0
    indx = df[df["Prop_of_genre_on_platf"] == 1.0].index
    df.drop(indx, inplace=True)
    df.to_csv('total_data_set.csv', index=False, encoding='utf-8')
