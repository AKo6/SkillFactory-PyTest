import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_1_all_pets_are_present(my_pets):
   """Проверка, что на странице со списком моих питомцев присутствуют все питомцы"""

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])
   number_of_pets = len(pets)

   assert number == number_of_pets
   print('Все питомцы присутствуют')

def test_2_half_has_photo(my_pets):
   """Проверка, что на странице со списком моих питомцев хотя бы у половины питомцев есть фото"""

   element = pytest.driver.implicitly_wait(5)

   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   half = number // 2

   number_а_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_а_photos += 1

   assert number_а_photos >= half
   print(f'количество фото: {number_а_photos}')
   print(f'Половина от числа питомцев: {half}')

def test_3_pets_have_NameAgeBreed(my_pets):
   """Проверка, что на странице со списком моих питомцев, у всех питомцев есть имя, возраст и порода"""

   element = pytest.driver.implicitly_wait(5)
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      result = len(split_data_pet)
      assert result == 3
      print('У всех питомцев есть данные')


def test_4_pets_have_different_names(my_pets):
   """Проверка, что на странице со списком моих питомцев у всех питомцев разные имена"""

   element = pytest.driver.implicitly_wait(10)
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   pets_name = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      pets_name.append(split_data_pet[0])

   # Перебираем имена и, если имя повторяется, то прибавляем к счётчику r единицу.
   # Проверяем если r == 0, то повторяющихся имён нет.
   r = 0
   for i in range(len(pets_name)):
      if pets_name.count(pets_name[i]) > 1:
         r += 1
   assert r == 0
   print(r)
   print(pets_name)


def test_5_no_repeating_pets(my_pets):
   """Поверка что на странице со списком моих питомцев нет повторяющихся питомцев"""

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   pet_data = pytest.driver.find_elements('css selector', '.table.table-hover tbody tr')

   list_data = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      list_data.append(split_data_pet)


   line = ''
   for i in list_data:
      line += ''.join(i)
      line += ' '

   list_line = line.split(' ')

   set_list_line = set(list_line)

   a = len(list_line)
   b = len(set_list_line)
   result = a - b
   assert result == 0
   print('Нет повторяющихся питомцев')





