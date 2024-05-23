import pandas as pd
import numpy as np

# ЭТО ШАГ 3 ГДЕ Я ЧИЩУ ДАННЫЕ
# наконец, надо совсместить спаршенные данные и исходные

with open("total_data_set.csv", "w", encoding="utf-8") as total:
    with open("try_more_data.csv", "r", encoding="utf-8") as ign:
        df1 = pd.read_csv(ign)
        df1 = df1.drop(np.where(df1['release_year'] == 2049)[0])
        # убираем все строки, где год выпуска 2049.
        # Это очевидный выброс, и он портит выборку
        df1 = df1.drop_duplicates(keep=False, inplace=False)
        df1.to_csv(total, encoding='utf-8', index=False)

    with open("ign.csv", "r", encoding="utf-8") as ign:
        df2 = pd.read_csv(ign)
        df2.drop(df2.columns[[0]], axis=1, inplace=True)
        df2.drop(['score_phrase', 'url', 'editors_choice', 'release_day'], axis=1, inplace=True)
        df2 = df2.drop_duplicates(keep=False, inplace=False) # это я пытаюсь убрать дубликаты
        df2 = df2.dropna() # убираем нулевые строки (только тут, так как в моём датасете таких не нашлось)
        df2.to_csv(total, encoding='utf-8', index=False)


# Далее просто проверяю, что файл открывается и читается без пропука строк.
# Когда я убежусь, что всё работает, приступлю к следующим шагам

with open("total_data_set.csv", "r", encoding="utf-8") as total:
    t = pd.read_csv(total)
    # print(sorted(t["release_year"].unique()))
    # отсюда выясняю, что моё исследование будет охватывать игры в период с 1994 по 2024 (год 1970 и 2049 учитываться
    # не будут. Очевидно это выбросы
    # далее я убрала все пропуски и повторения. Таким образом удалось убрать оставшиеся "проскочившие" фильмы и комиксы
    # print(t.isna().sum())
    # print(t.isnull().sum())
    # print(np.where(pd.isnull(t)))
    # print(t.info())


# Итого в моём датасете будет 21415 строк. Исходный датасет был обогащен на 6635 строк
# Ссылок получилось меньше (около 5к), так как у некоторых игр по несколько жанров - а значит и строк
