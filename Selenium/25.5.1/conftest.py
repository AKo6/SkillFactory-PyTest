import pytest
from settings import email, password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome(r'D:\Study_projects\Auto_Tests\selenium_auto_tests\driver_chrome\chromedriver.exe')
   pytest.driver.get('https://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


@pytest.fixture()
def my_pets():
   pytest.driver.find_element(By.ID,'email').send_keys(email)
   pytest.driver.find_element(By.ID,'pass').send_keys(password)
   pytest.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
   pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()
