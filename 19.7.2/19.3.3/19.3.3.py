import requests
import json
url = 'https://petstore.swagger.io/v2/'
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
info = {
      "id": 10,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }
status = 'available'
class Pet:
    """Everything about your Pets"""

    def post_pet(self):
        """Add a new pet to the store"""
        data = json.dumps(info, ensure_ascii=False)
        response = requests.post(f'{url}' + f'pet', headers=headers, data=data)
        return print(response.text, response.status_code)

    def put_pet(self):
        """Update an existing pet"""
        data = json.dumps(info, ensure_ascii=False)
        response = requests.put(f'{url}' + f'pet', headers=headers, data=data)
        return print(response.text, response.status_code)

    def get_pet_find_by_staus(self):
        """Finds Pets by status"""
        response = requests.get(f'{url}' + f'pet/findByStatus', params={'status': 'available'}, headers=headers)
        return print(response.text, response.status_code)

    def get_pet_id(self):
        """Find pet by ID"""
        response = requests.get(f'{url}' + f'pet/10', headers=headers)
        return print(response.text, response.status_code)

    def post_pet_id(self):
        """Updates a pet in store with form data"""
        params = {'petid':10, 'name':'fox', 'status':'available'}
        response = requests.post(f'{url}' + f'pet/10', params=params, headers=headers)
        return print(response.text, response.status_code)

    def delete_pet_id(self):
        """Delete a pet"""
        response = requests.delete(f'{url}' + f'pet/10', headers=headers)
        return print(response.text, response.status_code)


class Store:
    """Access to Petstore orders"""

    def post_store_order(self):
        """Place an order for a pet"""
        data = {
               "id": 5,
               "petId": 0,
               "quantity": 0,
               "shipDate": "2022-11-11T13:19:22.754Z",
               "status": "placed",
               "complete": True
        }
        data = json.dumps(data, ensure_ascii=False)
        response = requests.post(f'{url}' + 'store/order', headers=headers, data=data)
        return print(response.text, response.status_code)

    def get_store_order_id(self):
        """Find purchase order by ID"""
        response = requests.get(f'{url}' + f'store/order/5', headers=headers)
        return print(response.text, response.status_code)

    def delete_store_order_id(self):
        """Delete purchase order by ID"""
        response = requests.delete(f'{url}' + f'store/order/5', headers=headers)
        return print(response.text, response.status_code)

    def get_store_inventory(self):
        """Returns pet inventories by status"""
        response = requests.get(f'{url}' + f'store/inventory', headers=headers)
        return print(response.text, response.status_code)


class User:
    """Operations about user"""

    def post_user_create_with_array(self):
        """Creates list of users with given input array"""
        data = [
              {
               "id": 1,
               "username": "user1",
               "firstName": "string",
               "lastName": "string",
               "email": "string",
               "password": "string",
               "phone": "string",
               "userStatus": 0
              }
        ]
        data = json.dumps(data, ensure_ascii=False)
        response = requests.post(f'{url}' + 'user/createWithArray', headers=headers, data=data)
        return print(response.text, response.status_code)

    def post_user_create_with_list(self):
        """Creates list of users with given input array"""
        data = [
            {
                "id": 2,
                "username": "user2",
                "firstName": "string",
                "lastName": "string",
                "email": "string",
                "password": "string",
                "phone": "string",
                "userStatus": 0
            }
        ]
        data = json.dumps(data, ensure_ascii=False)
        response = requests.post(f'{url}' + 'user/createWithList', headers=headers, data=data)
        return print(response.text, response.status_code)

    def get_user_username(self):
        """Get users by user name"""
        params = 'user1'
        response = requests.get(f'{url}' + f'user/{params}', headers=headers)
        return print(response.text, response.status_code)

    def put_user_username(self):
        """Update user"""
        params = 'user1'
        data = [
            {
                "id": 1,
                "username": "user3",
                "firstName": "string",
                "lastName": "string",
                "email": "string",
                "password": "string",
                "phone": "string",
                "userStatus": 0
            }
        ]
        data = json.dumps(data, ensure_ascii=False)
        response = requests.put(f'{url}' + f'user/{params}', headers=headers, data=data)
        return print(response.text, response.status_code)

    def delete_user_username(self):
        params = 'user2'
        response = requests.delete(f'{url}' + f'user/{params}', headers=headers)
        return print(response.text, response.status_code)

    def get_user_login(self):
        """Logs user into the system"""
        params = {'username':'user1', 'password':'12345'}
        response = requests.get(f'{url}' + f'user/login{params}', headers=headers)
        return print(response.text, response.status_code)

    def get_user_logout(self):
        """Logs out current logged in user session"""
        response = requests.get(f'{url}' + f'user/logout', headers=headers)
        return print(response.text, response.status_code)

    def post_user(self):
        """Create user. This can only be done by the logged in user."""
        data = {
            "id": 0,
            "username": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        }
        data = json.dumps(data, ensure_ascii=False)
        response = requests.post(f'{url}' + f'user', headers=headers, data=data)
        return print(response.text, response.status_code)


print('Выполнение запросов к API для класса Pet')
Pet.post_pet(url)
Pet.put_pet(url)
Pet.get_pet_find_by_staus(url)
Pet.get_pet_id(url)
Pet.post_pet_id(url)
Pet.delete_pet_id(url)
print('Выполнение запросов к API для класса Store')
Store.post_store_order(url)
Store.get_store_order_id(url)
Store.delete_store_order_id(url)
Store.get_store_inventory(url)
print('Выполнение запросов к API для класса User')
User.post_user_create_with_array(url)
User.post_user_create_with_list(url)
User.get_user_username(url)
User.put_user_username(url)
User.delete_user_username(url)
User.get_user_login(url)
User.get_user_logout(url)
User.post_user(url)
