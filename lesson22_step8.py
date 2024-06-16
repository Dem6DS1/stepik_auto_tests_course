import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    # Открываем страницу
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("John")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Doe")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("john.doe@example.com")

    # Определяем путь к файлу в текущей директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")

    # Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Пауза для визуальной проверки результата
    time.sleep(10)

finally:
    # Закрываем браузер после всех манипуляций
    browser.quit()
