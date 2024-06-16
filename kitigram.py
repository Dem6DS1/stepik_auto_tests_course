import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

def generate_valid_username():
    # Генерируем случайное имя от 2 до 16 символов, состоящее только из латинских букв
    length = random.randint(2, 16)
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_valid_password():
    # Генерируем случайный пароль от 8 до 16 символов, содержащий хотя бы одну цифру, одну строчную, одну заглавную букву и один спецсимвол
    length = random.randint(8, 16)
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for i in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password) and
            ' ' not in password):
            return password

try:
    # Открываем страницу регистрации
    link = "https://kittygram-frontend-5.prakticum-team.ru/signup"
    browser = webdriver.Chrome()
    browser.get(link)

    # Пауза для полной загрузки страницы
    time.sleep(5)

    # Проверяем наличие и заполняем поле "имя"
    username = generate_valid_username()
    username_input = browser.find_element(By.NAME, "username")
    username_input.send_keys(username)

    # Проверяем наличие и заполняем поле "пароль"
    password = generate_valid_password()
    password_input = browser.find_element(By.NAME, "password")
    password_input.send_keys(password)

    # Проверяем наличие и заполняем поле "повторить пароль"
    confirm_password_input = browser.find_element(By.NAME, "password2")
    confirm_password_input.send_keys(password)

    # Отправляем заполненную форму
    submit_button = browser.find_element(By.CLASS_NAME, "button-form_button__4mpE0")
    submit_button.click()

# Пауза для полной загрузки страницы
    time.sleep(5)
 
finally:
       # Пауза для визуальной проверки результата
    time.sleep(10)

    # Закрываем браузер после всех манипуляций
    browser.quit()
