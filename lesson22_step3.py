import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Функция для вычисления суммы двух чисел
def calculate_sum(num1, num2):
    return num1 + num2

try:
    # Открываем страницу
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Пауза для полной загрузки страницы
    time.sleep(2)

    # Находим числа на странице
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    
    # Вычисляем сумму чисел
    total_sum = calculate_sum(num1, num2)
    
    # Выбираем значение в выпадающем списке, равное посчитанной сумме
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(total_sum))
    
    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Пауза для визуальной проверки результата
    time.sleep(10)

finally:
    # Закрываем браузер после всех манипуляций
    browser.quit()
