## Проект по Анализу данных 
## Тема "Анализ популярности игр на основе данных обзоров портала IGN"  (предварительная)

**<span style="color: green">ВАЖНО. Файл total_data_set.py - это уже исправленный датасет, 
финальный, без пропусков, выбросов и тд. Про то, как он редактировался я писала в 
README и в разных файлах по ходу работы</span>**

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

**<span style="color: green">ВАЖНО: после шага 5 решила доделать шаг 3, чтобы включить новые признаки тоже</span>**

* см. файл final_big_dataset.py
* файл ign_data.py нужен чтобы зафиксировать уникальные платформы и жанры
* см. файл Step3.py

В файле final_big_dataset.py я сливаю оба датасета (исходный и спаршенный) в один, в файл total_data_set.csv
Еще раз чищу все данные, убираю повторения, пропуски, и лишние стобцы в исходном датасете. 
Далее просто проверяю, что файл открывается и читается без пропука строк.

Какие признаки я взяла из исходного датасета: Название, Жанр, Платформа, Счет (оценка), Месяц и Год выпуска.
Брала их по двум причинам:
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

В файле Step3.py я описываю переменные в общем виде, как в семинаре:

Моя объясняемая переменная - это score, итоговый балл, который получила игра. 

Объясняющие переменные - все остальные. Среди них:
1) Категориальные: platform, genre, release_year, release_month
2) Непрерывные: score (из новых: Game_genre_rate,Prop_of_genre_on_platf,Mean_score_per_genre)

Первым делом я рассмотрела непрерывные переменные, пропусков в них не было, но выбросы нашлись. Удалила их.
Масштабироване признаков не делала, так как мне нет смысла приводить к одному масштабу признаки, ориентированные на 
разные по своей сути аспекты (пропорция и счет, например).

Для категориальных переменный я не делала бинаризацию признаков, потому что в каждой переменной у меня 
слишком много значений, будет странно разбивать один признак на 20 столбцов...

Подробнее про все описательные статистики в файле Step3.py. В нем я подробно расписываю, чо и зачем нахожу, какие выводы 
из этого делаю.

<u>**Шаг 4. Визуализация**</u>

* см. Файл Step4.py
* см. Файл no_multigenre.py (в этом файле убирала мультижанровость (Когда в колонке жанр стояло например "Action, Puzzle"))

Я рассмотрела попарно все признаки и после этого решила, что мне нужны дополнительные признаки.

- Я убрала мультижанровость, стало лучше, теперь мои графики выглядят не совсем как каша. Но... вам может показаться, что 
некоторые жанры игр нелепые, типа Number of players. Мне тоже так кажется, но я посмотрела, и такой реально есть,
вот тут игры этого жанра: https://www.ign.com/games/feature/number-of-players. 
Поэтому, если какой-то жанр кажется не уместным, или не жанром вообще, то все вопросы не ко мне, а к IGN, которые 
выделили такие жанры...

- Мне кажется мне нужны для исследования дополнительные признаки (см. далее в шаге 5)

Из визуализаций получилось узнать, какой жанр самый популярный, в какой месяц выставлялись самые высокие оценки, 
зависимость оценки от жанра и платформы. Я убрала мультижанровость, посмотрим, какие это дало результаты. 

Гипотезы, которые хочу проверить будут в шаге 6.

<u>**Шаг 5. Создание новых признаков**</u>

* см. файл Step5
* файл total_data_set - куда я в финале загружу новые признаки
* файл total_data_try - куда я в делаю пробные загрузки, чтобы не заруинить свой основной датасет и сэкономить время. (Наверное потом удалю, тк по факту это мусор)

<u>Какие хочу добавить  признаки?</u>

<span style="color: green">**Подробно про все признаки в файле Step5 по ходу решения**</span>

* Я добавила рейтинг жанра игры - "Game_genre_rate". Я вычислила отношение оценки игры к средней оценке для ее жанра.
Таким образом я хотела понять, насколько хорошо игра оценивается по сравнению с другими играми того же жанра.
  * Rоэффициент меньше 1 - значит игра хуже среднего, больше 1 - лучше среднего. Но мне кажется получалось не особо красиво. Я не знаю. как сделать красивее:(

* Я добавила относительную популярность жанра на платформе. Я вычислила долю игр каждого жанра на каждой платформе.
Это даст представление о том, какие жанры наиболее популярны на разных платформах и как эти предпочтения различаются.
Что значат циферки в этом признаке? Если, например, значение этого столбца 0.25, значит игры 
этого жанра составляют 25% всего контента на платформе.

* Я хочу добавить относительную оценку жанра на платформе. Я вычислю среднюю оценку для каждого жанра на каждой платформе,
а затем разделю ее на среднюю оценку по всем жанрам на этой платформе, чтобы посмотреть, какие жанры получают 
относительно высокие или низкие оценки на разных платформах.
Что значат циферки тут? Если оценка Жанра Экшн на платформе ПК равно 6, значит в среднем на пк игры в этом жанре оценивают на 6
При этом эта же игра, в этом же жанре но на платформе Айфон может быть оценена на 10. Я хочу использовать этот признак,
чтобы определить, на какую лучше платформу выпускать игру того или иного жанра. 


Пока что я не уверена, как именно будет происходить машинное обучение,
потому что после кр я поняла, что кажется я не совсем понимаю, как применять штуки из семинаров для реальных задач :(

Я нашла новые признаки, надеюсь я не ошиблась, и они правда будут мне полезны, и помогут мне с гипотезами.
Кстати о них...

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