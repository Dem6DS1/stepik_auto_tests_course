import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция для вычисления значения математической функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открыть страницу
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Проскроллить страницу вниз
    browser.execute_script("window.scrollBy(0, 100);")

    # Ввести ответ в текстовое поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # Выбрать checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Переключить radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажать на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Пауза для визуальной проверки результата
    time.sleep(10)

finally:
    # Закрыть браузер после всех манипуляций
    browser.quit()
