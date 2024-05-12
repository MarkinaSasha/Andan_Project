## Проект по Анализу данных 
## Тема "Анализ популярности игр на основе данных обзоров портала IGN"  (предварительная)

<u>**Шаг 0. Не поняла, как открыть ссылку прям с гитхаба**</u>

Когда датасет хранится на моем компе - всё работает. Когда я запушила всё на гитхаб - подставлять ссылку с гитхаба оказалось ошибкой. 
Но я не поняла, а как тогда обратиться к файлу на гитхабе...
```
Skipping line 41: ',' expected after '"'
Skipping line 1490: ',' expected after '"'
Skipping line 524: Expected 1 fields in line 524, saw 4
Skipping line 536: Expected 1 fields in line 536, saw 2
Skipping line 585: Expected 1 fields in line 585, saw 3
Skipping line 593: Expected 1 fields in line 593, saw 6
Skipping line 594: Expected 1 fields in line 594, saw 3
Skipping line 622: Expected 1 fields in line 622, saw 4
Skipping line 632: Expected 1 fields in line 632, saw 4
Skipping line 642: Expected 1 fields in line 642, saw 4
Skipping line 652: Expected 1 fields in line 652, saw 4
Skipping line 662: Expected 1 fields in line 662, saw 4
Skipping line 672: Expected 1 fields in line 672, saw 4
Skipping line 682: Expected 1 fields in line 682, saw 4
Skipping line 692: Expected 1 fields in line 692, saw 4
Skipping line 707: Expected 1 fields in line 707, saw 4
Skipping line 711: Expected 1 fields in line 711, saw 4
Skipping line 718: Expected 1 fields in line 718, saw 4
Skipping line 725: Expected 1 fields in line 725, saw 4
Skipping line 747: Expected 1 fields in line 747, saw 4
Skipping line 751: Expected 1 fields in line 751, saw 4
Skipping line 755: Expected 1 fields in line 755, saw 4
Skipping line 759: Expected 1 fields in line 759, saw 4
Skipping line 771: Expected 1 fields in line 771, saw 4
Skipping line 775: Expected 1 fields in line 775, saw 4
Skipping line 779: Expected 1 fields in line 779, saw 4
Skipping line 791: Expected 1 fields in line 791, saw 4
Skipping line 798: Expected 1 fields in line 798, saw 8
Skipping line 799: Expected 1 fields in line 799, saw 3
Skipping line 805: Expected 1 fields in line 805, saw 4
Skipping line 809: Expected 1 fields in line 809, saw 4
Skipping line 830: Expected 1 fields in line 830, saw 4
Skipping line 841: Expected 1 fields in line 841, saw 4
Skipping line 853: Expected 1 fields in line 853, saw 4
Skipping line 857: Expected 1 fields in line 857, saw 4
Skipping line 861: Expected 1 fields in line 861, saw 4
Skipping line 869: Expected 1 fields in line 869, saw 3
Skipping line 884: Expected 1 fields in line 884, saw 2
Skipping line 901: Expected 1 fields in line 901, saw 5
Skipping line 1168: Expected 1 fields in line 1168, saw 2
Skipping line 1234: Expected 1 fields in line 1234, saw 2
Skipping line 1254: Expected 1 fields in line 1254, saw 6
Skipping line 1255: Expected 1 fields in line 1255, saw 3
Skipping line 1261: Expected 1 fields in line 1261, saw 6
Skipping line 1262: Expected 1 fields in line 1262, saw 3
Skipping line 1310: Expected 1 fields in line 1310, saw 2
Skipping line 1331: Expected 1 fields in line 1331, saw 6
Skipping line 1337: Expected 1 fields in line 1337, saw 6
Skipping line 1345: Expected 1 fields in line 1345, saw 6
Skipping line 1365: Expected 1 fields in line 1365, saw 4
Skipping line 1373: Expected 1 fields in line 1373, saw 4
Skipping line 1381: Expected 1 fields in line 1381, saw 4
Skipping line 1389: Expected 1 fields in line 1389, saw 4
Skipping line 1397: Expected 1 fields in line 1397, saw 4
Skipping line 1405: Expected 1 fields in line 1405, saw 4
Skipping line 1413: Expected 1 fields in line 1413, saw 4
Skipping line 1544: Expected 1 fields in line 1544, saw 2
Skipping line 1551: Expected 1 fields in line 1551, saw 3
Skipping line 1554: Expected 1 fields in line 1554, saw 3
Skipping line 1557: Expected 1 fields in line 1557, saw 3
Skipping line 1560: Expected 1 fields in line 1560, saw 3
Skipping line 1563: Expected 1 fields in line 1563, saw 3
Skipping line 1566: Expected 1 fields in line 1566, saw 3
Traceback (most recent call last):
  File "D:\Anaconda\lib\site-packages\pandas\core\indexes\base.py", line 3629, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 136, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 163, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'score'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Саша\Python_Basic\Andan_project\Step4.py", line 52, in <module>
    ser = pd.Series(df['score'])
  File "D:\Anaconda\lib\site-packages\pandas\core\frame.py", line 3505, in __getitem__
    indexer = self.columns.get_loc(key)
  File "D:\Anaconda\lib\site-packages\pandas\core\indexes\base.py", line 3631, in get_loc
    raise KeyError(key) from err
KeyError: 'score'
```


<u>**Шаг 1. Выбор темы**</u>

    Почему решила делать одна:

    1) Когда огласили условие, что каждый член команды должен понимать и уметь объяснить каждую строчку кода, 
    я сразу поняла, что буду делатб всё одна. Я не готова сидеть и долго объяснять свой код другим, 
    или вникать в то, как пишут мои друзья (я знаю как они пишут, и мне не нравится)
    Мне кажется безопаснее сделать самому, чтобы если уж руинить, то самостоятельно.
    
    2) Если я буду делать все этапы сама, я смогу лучше разобраться теме, и больше шансов, что я запомню все этапы
    и смогу в будущем применять эти знания

<u>**Шаг 2. Сбор данных**</u>

Давайте начнем с самого начала.
Первым делом я пошла на сайт https://www.kaggle.com/datasets/joebeachcapital/ign-games/data?select=ign.csv и просто забрала оттуда датасет
Далее мне нужно было его обогатить, поскольку там данные только про игры до 2016 года. Я отправилась на сайт https://www.ign.com/reviews. 

* см. Файл parsing_links

Я решила парсить сайт со всеми обзорами, а не только игровыми, так как страница с игровыми обзорами не парсилась дальше 17-ой страницы. 
Я не смогла найти решение, поэтому пошла через главную страницу. Через fake_useragent получается обмануть сайт, тут не пришлось выдумывать каких-то сложных масок.

Далее я столкнулась с проблемой - сайт не имеет явных страниц, его надо прокручивать. Немного поборовшись с ним, получилось сделать то, что мне нужно.
Но возникла новая проблема - сайт парсится долго, а сколько конкретно мне нужно прокруток я не знаю. Поставила 600 наугад, потому что вручную прокрутить и проверить было бы еще сложнее
В итоге я смогла собрать данные по всем недостающим мне годам (получилось, что дата обзора не совпадала с датой выхода, что, наверное, должно было быть очевидно,
так что у меня появилось 5352 новых ссылок, которые покрыли вообще все годы с 1994 до 2024)

* см. файл ign_links_more.txt. Тут все ссылки, которые удалось получить
* Исходный датасет в файле ign.csv

Теперь из всех ссылок надо составить единый датасет. 

* см. файл making_df.py

Для того, чтобы почистить датасет от всех НЕигр я делала кучу дополнительных проверок. 
Фишку про трансформирование с json string  посмотрела тут  https://ru-brightdata.com/blog/how-tos-ru/parse-json-data-with-python
На все пустые места ставила "---", чтобы потом зачесть их как пропуски и вообще убрать из датасета.
Много раз идет пофторение 

```
platform_data = np.append(platform_data, "---")
year_data = np.append(year_data, "---")
month_data = np.append(month_data, "---")
```
Но я не придумала, как сделать это красивее.
Суммарно парсила сайт 2 дня. Финальный парсинг занял 4 часа.

* Все данные были перенесены в файл try_more_data.csv. Теперь надо влить ее в основной датасет



**<span style="color: green">ВАЖНО: Помогите пожалуйста, мой датасет почему-то не хочет работать, если я убираю из него строку с заголовком (у меня он продублировался при сливании в общий файл)
Что делать?</span>**



<u>**Шаг 3. Предварительная обработка**</u>

* см. файл final_big_dataset.py
* файл ign_data.py нужен чтобы зафиксировать уникальные платформы и жанры

В этом файле я сливаю оба датасета (исходный и спаршенный) в один, в файл total_data_set.csv
Еще раз чищу все данные, убираю повторения, пропуски, и лишние стобцы в исходном датасете. Далее просто проверяю, что файл открывается и читается без пропука строк.

Какие признаки я взяла: Название, Жанр, Платформа, Счет (оценка), Месяц и Год выпуска. Брала их по двум причинам:
- В исходном датасете есть колонки: url, score_phrase и editors_choice, которые, как мне кажется, никак не обогащают датасет
- Я не смогла понять, как и откуда с сайта IGN напарсить editors_choice, поэтому я просто не могу его добавить.

Я предпочла удалять строки с любым количеством пропусков, по двум причинам:
- Если данные отсутствуют - это не обзор компьютерной игры, а фильма, 
  статьи или настольной игры (следовательно все такие варианты я сразу отсеила в рамках "Фильтрации данных")
- В моем датасете ставить в пропуски средние значение - некорректно. Как можно поставить среднее из игровых платформ? 
  Или среднюю оценку игр? Цель моего исследования найти возможную взаимосвязь 
  между датой выхода, жанром, оценкой и платформой. Делать эти значения рандомными = "средними" - это означает испортить выборку


Итого в моём датасете будет 21415 строк. Исходный датасет был обогащен на 6635 строк
Ссылок получилось меньше (около 5к), так как у некоторых игр по несколько жанров - а значит и строк

<u>**Шаг 4. Визуализация**</u>

* см. Файл Step4

Я рассмотрела попарно все признаки и после этого решила, что мне нужны дополнительные признаки.
Во-первых, надо будет еще раз доработать сам датасет, подкорректироват жанры и убрать мультижанровость.
Во-вторых, мне кажется мне нужны для исследования дополнительные признаки (см. далее в шаге 5)

Из визуализаций получилось узнать, какой жанр самый популярный, в какой месяц выставлялись самые высокие оценки, 
зависимость оценки от жанра и платформы (опять же, когда уберу мультижанровость, думаю, будут более явные результаты).

Гипотезы, которые хочу проверить будут в шаге 6.

<u>**Шаг 5. Создание новых признаков**</u>

* см. файл Step5
* файл total_data_set - куда я в финале загружу новые признаки
* файл total_data_try - куда я в делаю пробные загрузки, чтобы не заруинить свой основной датасет и сэкономить время.

<u>Какие хочу добавить  признаки?</u>

* Я добавила рейтинг жанра игры - "Game_genre_rate". Я вычислила отношение оценки игры к средней оценке для ее жанра.
Таким образом я хотела понять, насколько хорошо игра оценивается по сравнению с другими играми того же жанра.
  * Пока я добавила только его. Получилось как я задумывала: коэффициент меньше 1 - значит игра хуже среднего, больше 1 - лучше среднего. Но мне кажется получалось не особо красиво. Я не знаю. как сделать красивее:(
* Я хочу добавить относительную популярность жанра на платформе. Я вычислю долю игр каждого жанра на каждой платформе.
Это даст вам представление о том, какие жанры наиболее популярны на разных платформах и как эти предпочтения различаются.
* Я хочу добавить относительную оценку жанра на платформе. Я вычислю среднюю оценку для каждого жанра на каждой платформе,
а затем разделю ее на среднюю оценку по всем жанрам на этой платформе, чтобы посмотреть, какие жанры получают относительно высокие или низкие оценки на разных платформах.

Пока первого признака нет в основном датасете, чтобы потом я могла влить все три новых сразу

Я надеюсь эти признаки будут действительно полезными и помогут мне с моими гипотезами. Кстати о них

<u>**Шаг 6. Гипотезы**</u>

<u>Какие гипотезы хочу проверить?</u>
* Игры определенных жанров (например, ролевые игры или экшены) получают более высокие оценки, чем игры других жанров
Как раз мне для этого нужны будут мои новые признаки, так как они позволят учесть взаимоотношение жанра и лпатформы
* Игры, выпущенные на определенных платформах (например, ПК или консоли), 
получают более высокие оценки, чем игры, выпущенные на других платформах
* Игры с более высокими оценками имеют более высокий рейтинг игры/жанра (отношение оценки игры к средней оценке для ее жанра)
* Средняя оценка по жанру и платформе различается для разных комбинаций жанра и платформы. Интересно проверить, на сколько и связано ли это как-то с оценкой

Вроде пока что это все гипотезы, которые я хотела бы проверить. На основе результатов я хочу попытаться определить,
в каком жанре, на какой платформе и в какое время лучше всего выпускать игру, чтобы она с наибольшей вероятностью получила высокую оценку.