import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
import re
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
import kaggle
import time
import json
# С сайта https://selenium-python.readthedocs.io/getting-started.html#simple-usage
# на всякий случай предварительно качаю всё
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ign_data import find_u_gen
from ign_data import find_u_pltf

unique_genres = find_u_gen()
unique_platforms = find_u_pltf()

# Далее будет достаточно много проверок. Страница с обзорами конкретно на игры не грузится дальше 17-ой страницы
# Поэтому пришлось парсить главную страницу со всеми обзорами. Таким образом у меня собрались ссылки вообще про всё
# Игры, фильмы и тд. Но мне нужны только игры. Поэтому я для каждого параметра (имя, счет, жанр, платформа) добавляла
# Доп проверки, так как у фильмов, например, точно не будет указана платформа (типа РС или Хbox).
# Таким образом я старалась отсеять лишние данные, которые точно не игры (тем же способом отсеялись и настолки, так как
# у них пропадает параметр имени). Возможно есть и более простой способ, но я не смогла его реализовать.

name_data = np.array([])
platform_data = np.array([])
score_data = np.array([])
genre_data = np.array([])
year_data = np.array([])
month_data = np.array([])

used_genres = np.array([])
# теперь необходимо перейти по всем этим ссылкам. Дальше я буду работать отдельно с каждой страницей.

#
with (open("ign_links_more.txt", "r", encoding="utf-8") as ign):
    for link in ign:
        url = link.strip()  # На всякий случай почитила ссылки от лишних символов (типа \n в конце).
        # Без стрипа выдает 404
        resp = requests.get(url, headers={'User-Agent': UserAgent().chrome})
        page_info = BS(resp.content, "html.parser")

        # Тут достаем имя
        try:
            name_info = page_info.find("a", {"class": "jsx-4245402894 article-object-link underlined"})
            name_data = np.append(name_data, name_info.text)
            print(name_info.text)
        except Exception:
            name_data = np.append(name_data, "---")
            print("No name")

        # достанем счет
        try:
            score_info = page_info.find_all("div", {"class": "stack jsx-868863109 review-score-section"})
            game_score = score_info[0].div.figcaption.text
            score_data = np.append(score_data, game_score)
        except:
            score_data = np.append(score_data, "---")
            continue

        # Имя и счет достали. Дальше достаем игровую платформу, дату, жанр
        # Важно доставать платформу в последнюю очередь, потому что так удобнее вносить в таблицу
        platform_info = page_info.find_all("script", {"id":"__NEXT_DATA__"})
        for script in platform_info:
        # JSON string   ---  https://ru-brightdata.com/blog/how-tos-ru/parse-json-data-with-python
            script = script.text
            # from JSON string to Python dict
            script_dict = json.loads(script)
            # verify the type of the resulting variable
            info_str = script_dict["props"]["pageProps"]["page"]["attributes"]
            if len(info_str) > 0:
                for elem in info_str:
                    try:
                        game_genre = elem["attribute"]['name']
                        if game_genre in unique_genres:
                            genre_data = np.append(genre_data, game_genre)
                            break
                        else:
                            genre_data = np.append(genre_data, "---")
                            break
                    except Exception:
                        game_genre = "---"
                        genre_data = np.append(genre_data, "---")
                        break
            else:
                game_genre = "---"
                genre_data = np.append(genre_data, "---")
            #достаем отсюда данные о платформах, на которых выпустится игра, год и месяц релиза и жанр
            release_genre_str = script_dict["props"]["pageProps"]["page"]["primaryObject"]["objectRegions"]
            # проверки для года, месяца, платформы
            # тут будет очень много проверок. Они могут показаться не нужными, но так вышло, потому что
            # я парсила две разные страницы (общие обзоры и только игровые), которые отличалесь по своей структуре
            # пришлось добавить несколько доп проверок
            if release_genre_str and len(release_genre_str) > 0:
                try:
                    for elem in release_genre_str:
                        date_list = []
                        platf_list = []
                        for i_elem in elem["releases"]:
                            platf_list.append(i_elem["platformAttributes"][0]["name"])
                            date_list.append(i_elem["date"])

                        date_list = [x for x in date_list if x is not None]
                        platf_list = [x for x in platf_list if x is not None]
                        release_date = max(date_list).split("-")

                        year = str(release_date[0])
                        month = str(int(release_date[1]))
                        # вот тут будем делать доп строки в случае, если игра на нескольких платформах
                        # убираем мультиплатформы и те, которых нет в исходном датасете
                        for i in platf_list:
                            if i not in unique_platforms:
                                platf_list.remove(i)

                        if len(platf_list) > 0:
                            for i_elem in range(0, len(platf_list)):
                                platform_data = np.append(platform_data, platf_list[i_elem])
                                year_data = np.append(year_data, year)
                                month_data = np.append(month_data, month)

                            for i_elem in range(0, len(platform_data) - len(name_data)):
                                name_data = np.append(name_data, name_info.text)
                                score_data = np.append(score_data, game_score)
                                genre_data = np.append(genre_data, game_genre)

                        else:
                            platform_data = np.append(platform_data, "---")
                            year_data = np.append(year_data, "---")
                            month_data = np.append(month_data, "---")
                except:
                    platform_data = np.append(platform_data, "---")
                    year_data = np.append(year_data, "---")
                    month_data = np.append(month_data, "---")
                    # На сайте указано много дат - для каждой платформы своя. Поэтому я решила брать самую
                    # позднюю дату (чтоб наверняка)

            else:
                platform_data = np.append(platform_data, "---")
                year_data = np.append(year_data, "---")
                month_data = np.append(month_data, "---")
        print("-" * 30)


# Итак, все данные для обогащения датасета собраны. Теперь надо собрать их в единую таблицу.
# каждый раз проверяла длину строк, чтобы финальный датасет не полетел
# print(len(name_data))
# print(len(platform_data))
# print(len(score_data))
# print(len(genre_data))
# print(len(year_data))
# print(len(month_data))

# суммарно парсила сайт 2 дня. Финальный парсинг занял 4 часа.
df = pd.DataFrame({"title":name_data, "platform":platform_data,
                   "score":score_data, "genre":genre_data,
                   "release_year":year_data, "release_month":month_data})
df = df[df.isin(["---"]) == False]
df = df.dropna()
df.to_csv (r'C:\Users\Саша\Python_Basic\Andan_project\try_more_data.csv', index= False )
