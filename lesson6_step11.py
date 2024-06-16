from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Тест для первой страницы
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных полей
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class .third")
    input3.send_keys("ivan.petrov@example.com")

    # Отправка заполненной формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверка, что регистрация прошла успешно
    time.sleep(5)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

try:
    # Тест для второй страницы
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных полей
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class .third")
    input3.send_keys("ivan.petrov@example.com")

    # Отправка заполненной формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверка, что регистрация прошла успешно
    time.sleep(5)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
