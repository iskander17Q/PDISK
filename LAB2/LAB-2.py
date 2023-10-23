import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def create_directory(folder):
    os.makedirs(folder, exist_ok=True)

def scroll_page(driver, num_images):
    # Оптимизированный код для скроллинга
    pass

def download_image(url, folder, filename):
    # Оптимизированный код для загрузки изображения
    pass

def download_images(query, folder, num_images):
    create_directory(folder)
    driver = webdriver.Chrome()
    driver.get(f"https://yandex.ru/images/search?text={query}")
    scroll_page(driver, num_images)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    thumbnails = soup.find_all("img", class_="serp-item__thumb")

    count = 0
    for thumbnail in thumbnails[:num_images]:
        full_image_url = "https:" + thumbnail["src"]
        filename = f"{str(count).zfill(4)}.jpg"
        download_image(full_image_url, folder, filename)
        count += 1

    driver.quit()

download_images("polar bear", "dataset/polar_bear", 1000)
download_images("brown bear", "dataset/brown_bear", 1000)