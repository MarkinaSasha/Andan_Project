import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings("ignore")


uni_gen_dict = {}  # этот словарь для моего первого нового признака: Game_genre_rate
num_gen = {}

# Первым делом соберу все данные о всех оценках во всех жанрах.
with open("C:/Users/Саша/Python_Basic/Andan_project/total_data_set.csv", "r", encoding='utf-8') as ign:
    text = pd.read_csv(ign)
    # print(text['genre'], text['score'])
    # тут для посчитаем количество игр каждого жанра
    n = 0
    for i_gen in text['genre']:
        try:
            if i_gen not in num_gen:
                num_gen[i_gen] = 0
            num_gen[i_gen] += 1
        except (KeyError, ValueError, TypeError):
            continue
        n += 1

    n = 0
    # Тут для каждого жанра посчитаем общий счет
    for i_gen in text['genre']:
        try:
            if i_gen not in uni_gen_dict:
                uni_gen_dict[i_gen] = 0
            uni_gen_dict[i_gen] += float(text.iloc[[n]]['score'])
        except (KeyError, ValueError, TypeError):
            continue
        n += 1

    # Наконец найдем среднее
    mean_rate_dict = {}
    for i in num_gen.keys():
        mean_rate_dict[i] = uni_gen_dict[i]/num_gen[i]

    # Отлично, у меня есть средняя оценка для каждого жанра игр


# Теперь буду искать относительную для каждого жанра оценку.

with open("C:/Users/Саша/Python_Basic/Andan_project/total_data_set.csv", "r", encoding='utf-8') as ign:
    text = pd.read_csv(ign)
    n = 0
    coeff_list = []
    score_list = []
    name_list = []

    # Сделаю лист со всеми счетами каждой игры
    for i_score in text['score']:
        try:
            score_list.append(i_score)
        except:
            score_list.append("None")
    # Сделаю список с названием жанра каждой игры
    for i_name in text['genre']:
        try:
            name_list.append(i_name)
        except:
            name_list.append("None")

    # Мои списки одинаковы по длине, так что теперь я спокойно могу их использовать и сопоставлять с финальной таблицей
    n = 0
    for i_name in name_list:
        try:
            total_genre_rate = mean_rate_dict[i_name]
            coeff = float(score_list[n])/float(total_genre_rate)
        except:
            coeff = "Game_genre_rate"
        coeff_list.append(coeff)
        n += 1

    text["Game_genre_rate"] = coeff_list
    text.to_csv("C:/Users/Саша/Python_Basic/Andan_project/total_data_set.csv", index=False, encoding='utf-8')

    # Итак, я добавила первый новый признак, который в дальнейшем хочу использовать для своих вычислений.
    # Осталось еще два.
    # Продолжение следует...


