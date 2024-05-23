import pandas as pd

import warnings
warnings.filterwarnings("ignore")


uni_gen_dict = {}  # этот словарь для моего первого нового признака: Game_genre_rate
num_gen = {}

# Первый новый признак
# ____________________________________________________________________________________________________________
# Первым делом соберу все данные о всех оценках во всех жанрах.
with open("total_data_set.csv", "r", encoding='utf-8') as ign:
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

with open("total_data_set.csv", "r", encoding='utf-8') as ign:
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
#     # Сделаю список с названием жанра каждой игры
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
            coeff = round(float(score_list[n])/float(total_genre_rate), 3)
        except:
            coeff = "Game_genre_rate"
        coeff_list.append(coeff)
        n += 1

    text["Game_genre_rate"] = coeff_list
    text.to_csv("total_data_set.csv", index=False, encoding='utf-8')

    # Итак, я добавила первый новый признак, который в дальнейшем хочу использовать для своих вычислений.
    # Осталось еще два.

# Второй новый признак
# ____________________________________________________________________________________________________________

# А вот и продолжение. Итак, второй признак, который я хочу добавить - это популярность жанра на платформе.
# Я вычислю долю игр каждого жанра на каждой платформе.

platf_dict = {}  #{platform : {genre: number}}
coeff_dict = {} # {platform : {genre: proportion on platform}}

with open("total_data_set.csv", "r", encoding='utf-8') as ign:
    text = pd.read_csv(ign)
    for platf in text['platform']:
        if platf not in platf_dict:
            platf_dict[platf] = {}
            coeff_dict[platf] = {} # понадобится дальше
    for key_platf in platf_dict.keys():
        for genre in text[text['platform'] == key_platf]['genre']:
            if genre not in platf_dict[key_platf]:
                coeff_dict[key_platf][genre] = 0
                platf_dict[key_platf][genre] = 0
            platf_dict[key_platf][genre] = platf_dict[key_platf].get(genre, 0) + 1

# Что мы получили? Мы получили словарь, с каждой платформой. В каждом словаре еще словарь,
# в котором написано количество игр каждого жанра на этой платформе.
# Теперь я хочу рассчитать долю каждого жанра на каждой платформе.

for platf in platf_dict.keys():
   all_nums = sum(list(platf_dict[platf].values())) # Найдем всего жанров / игр на платформе
   for genre in platf_dict[platf]:
       genre_coeff = platf_dict[platf][genre] / all_nums # количество игр жанра делю на общее кол-во игр
       coeff_dict[platf][genre] = genre_coeff

# Наконец добавим новый стобец

prop_list = []
with open("total_data_set.csv", "r", encoding='utf-8') as ign:
    text = pd.read_csv(ign)
    for game in text.iloc:
        platf = game['platform']
        genre = game['genre']
        score = round(coeff_dict[platf][genre], 3)
        prop_list.append(score)

    text['Prop_of_genre_on_platf'] = prop_list
    text.to_csv("total_data_set.csv", index=False, encoding='utf-8')

# Что я получила? Prop_list это список с пропорциями жанров на каждой платформе. Если, например, значение
# этого столбца 0.25, значит игры этого жанра составляют 25% всего контента на платформе.


# Третий новый признак
# ____________________________________________________________________________________________________________

# Ура, остался последний признак. В качестве третьего признака
# Я хочу добавить относительную оценку жанра на платформе.
# Я вычислю среднюю оценку для каждого жанра на каждой платформе,
# а затем разделю ее на среднюю оценку по всем жанрам на этой платформе, чтобы посмотреть, какие жанры
# получают относительно высокие или низкие оценки на разных платформах.

# названия тут похожи, это может путать, но назвать по-другому никак, потому что это буквально еще один словарь
# с пратформами, но немножко другой...

platformdict = {}  #{platform : {genre: summ_score_rates}}

with open("total_data_set.csv", "r", encoding='utf-8') as ign:
    text = pd.read_csv(ign)
    for platf in text['platform']:
        if platf not in platformdict:
            platformdict[platf] = {}
    for key_platf in platformdict.keys():
        for genre in text[text['platform'] == key_platf]['genre']:
            if genre not in platformdict[key_platf]:
                total_gen_sum = platf_dict[key_platf][genre]
                platformdict[key_platf][genre] = text[text['platform'] == key_platf][text['genre'] == genre]['score'].sum() / total_gen_sum

    # Итак, мы получили словарь, где для каждой платформы есть словарь с жанрами на ней, со средней оценкой этого жанра
    # на этой платформе
    # пример: {'PlayStation Vita': {'Action': 9.0, 'Platformer': 9.0}}. Это значит, что средняя оценка Экшнов
    # на Плэйстэйшне Вита - 9.
    # Теперь занесем это всё в total_data_set.csv
    mean_gen_score = []
    for game in text.iloc:
        platf = game['platform']
        genre = game['genre']
        score = round(platformdict[platf][genre], 3)
        mean_gen_score.append(score)
    text['Mean_score_per_genre'] = mean_gen_score
    text.to_csv("total_data_set.csv", index=False, encoding='utf-8')

# Ура! Вот и все доп признаки, которые я хотела добавить.
