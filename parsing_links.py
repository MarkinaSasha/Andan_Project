import requests
from fake_useragent import UserAgent
import time

# С сайта https://selenium-python.readthedocs.io/getting-started.html#simple-usage
# на всякий случай предварительно качаю всё
from selenium import webdriver
from selenium.webdriver.common.by import By
from ign_data import find_u_gen
from ign_data import find_u_pltf

unique_genres = find_u_gen()
unique_platforms = find_u_pltf()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}
url = "https://www.ign.com/reviews"

# для того, чтобы начать парсинг, я буду использовать модуль fake_useragent. Иначе выдает ошику 403
# response = requests.get(url) #, headers={'User-Agent': UserAgent().chrome})
# print(response.status_code)
# теперь другое дело
response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
# print(response.status_code)

# tree = BS(response.content, "html.parser")
# start_info = tree.find_all('a', {'class': "item-body"})
# однако тут всплывает новая проблема. Сайт который я хочу парсить - динамический. То есть он прогружается при скролинге
# Это очень печально, потому что тут даже нельзя пощелкать страницы, чтобы найти их значения. Но я не отчаиваюсь
# и иду в интернет искать, что делать. Мне повезло - на сайте IGN нет явной пагинации, спасибо...
# Принято решение использовать селениум
# Устанавливаю
# Нужно настроить связь питона и браузера, поэтому:
#************************************
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={UserAgent().random}")
driver = webdriver.Chrome(options=options)
driver.get(url)

# так как у меня динамический сайт, делаю вот так: https://digitalsfera.ru/prokrutka-stranitsy-v-selenium-python
# я взяла код отсюда, добавила ограничение на количество страниц, потому что мне нужны не все, а только до 2016 года
# также я добавила в конец скрипт для записи всех ссылок в отдельный файл ign_links_more.txt
last_height = driver.execute_script("return document.body.scrollHeight")
pages = [i for i in range(20)]
n = 0
while n < 600:
    # Прокрутка вниз
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Пауза, пока загрузится страница.
    # Вычисляем новую высоту прокрутки и сравниваем с последней высотой прокрутки.
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    n += 1
    print(n)
    print(last_height, new_height)
    last_height = new_height

with open("ign_links_more.txt", "w", encoding="utf-8") as ign:
    # найдем все ссылки на каждую страницу и сложим их в новый файл
    start_info = driver.find_elements(By.CLASS_NAME, "item-body")
    for string in start_info:
        href = string.get_attribute("href")
        ign.write(href + "\n")