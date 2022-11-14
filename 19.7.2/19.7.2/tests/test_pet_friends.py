
from api import PetFriends
from settings import *
import os.path

pf = PetFriends()

def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """ Проверяем что запрос api ключа для несуществующего пользователя не возвращает статус 200
    и в результате не содержится слово key"""

    status, result = pf.get_api_key(email, password)

    assert status != 200
    assert 'key' not in result


def test_unsuccess_get_all_pets_for_invalid_user(filter=''):
    """ Проверяем невозможность получить список питомцев без ключа.
    Доступное значение параметра filter - 'my_pets' либо '' """

    auth_key = {'key': ''}
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 403
    assert 'Please provide &#x27;auth_key&#x27; Header' in result


def test_add_new_pet_with_special_characters(name='!@#$%^&*()', animal_type='_+/*-+|?\\',
                                     age='ten', pet_photo='image/mr-poopybutthole.jpg'):
    """Проверяем что можно добавить питомца с некорректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_whitespace_info(name='', animal_type='',
                                     age='', pet_photo='image/corgi.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_valid_data_twice(name='Mr.PoopyButtHole', animal_type='Alien',
                                     age='40', pet_photo='image/mr-poopybutthole.jpg'):
    """Проверяем что можно добавить питомца с корректными данными дважды"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Дублируем добавление питомца
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert result['name'] == name

def test_delete_all_my_pet():
    """Проверяем возможность удаления всех своих питомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet_id = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(pet_id['pets']) != 0:
        for i in range(len(pet_id['pets'])):
            _, result = pf.delete_pets(auth_key, pet_id['pets'][i]['id'])

    _, pet_id = pf.get_list_of_pets(auth_key, '')
    status, result = pf.delete_pets(auth_key, pet_id['pets'][0]['id'])

    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    assert status == 200
    assert pet_id['pets'][0]['id'] not in my_pets.values()


def test_successful_add_pet_simple(name='Суперпес', animal_type='Королевский корги',
                                     age='2'):
    """Проверяем возможность добавления питомца без фотографии"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_successful_add_pet_simple_with_long_text(name='Суперпес'*30, animal_type='wt&'*30,
                                     age=''):
    """Проверяем возможность добавления питомца без фотографии c большой длинной данных"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_successful_add_photo_of_pet(pet_photo='image/corgi.jpg'):
    """Проверяем, что можно добавить фото питомца"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) == 0:
        pf.post_add_new_pet_simple(auth_key, 'Суперпес', 'королевский корги', '2')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    status, result = pf.post_add_photo(auth_key, pet_id, pet_photo)

    assert status == 200
    assert len(result['pet_photo']) > 0

def test_update_pet_info_for_all_my_pets(name='LoL', animal_type=':)', age=50):
    """Проверяем возможность обновления информации о питомце"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")


    if len(my_pets['pets']) > 0:
        for i in range(len((my_pets['pets']))):
            status, result = pf.put_update_pet_info(auth_key, my_pets['pets'][i]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")