import pandas as pd

# Итак, мне не понравилась мультижаноровость, которую я забыла убрать на предыдущих шагах.
# Поэтому буду убирать ее здесь. Я решила, что я прочешу файл, соберу все жанры, везде, где их два, сделаю один.
# После этого запихну всё в список, и сделаю новых стобец в датафрейме single_genre_table. После этого добавлю
# этот столбец в мой исходный датафрем вместо столбца genre.
# Я боюсь, что таким образом я очень нагружу комп, потому что хранить список из 25к значений звучит ужасно.
# Но я не придумала, как сделать лучше, буду признательна, если дадите коментарии по этому моменту, потому что
# пока что выглядит прям не оч((

with open("total_data_set.csv", 'r+', encoding='utf-8') as file:
    df = pd.read_csv(file, engine='python')
    # df['genre'].isna().sum()  проверила, что нет пропусков, чтобы избежать лишних ошибок
    print(df['genre'])
    single_genre_table = pd.DataFrame()
    safe_list = []
    for i in df['genre']:
        safe_list.append(i.split(",")[0])
    single_genre_table['single_genre'] = safe_list
    df['genre'] = single_genre_table['single_genre']
    df.to_csv('total_data_set.csv', index=False, encoding='utf-8')


