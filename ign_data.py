import pandas as pd

""" Этот модуль нужен для того, чтобы брать из исходного файла данные о жанре и платформах
чтобы в дальнейшем все мои собранные данные не отличались по набору характеристик от исходника"""

def find_u_gen():
    with open("ign.csv", "r", encoding="utf-8") as ign:
        df = pd.read_csv(ign)
        # pd.options.display.max_columns = len(df.columns)
        # полюбовались датасетом и хватит-
        # pd.set_option('display.max_columns', None)
        # print(df.head())

        unique_genres = list(df["genre"].unique())
        uni_gen = [x for x in unique_genres if isinstance(x, str) and ", " not in x]
    return uni_gen


def find_u_pltf():
    with open("C:/Users/Саша/Python_Basic/Andan_project/ign.csv", "r", encoding="utf-8") as ign:
        df = pd.read_csv(ign)
        unique_pltf = list(df["platform"].unique())
        uni_pl = [x for x in unique_pltf if isinstance(x, str)]
    return uni_pl

