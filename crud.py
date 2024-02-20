import requests
class Crud:
    BASE_URL = '<https://parseapi.back4app.com/classes/>'
    HEADERS = {
        'X-Parse-Application-Id': 'APP_ID',
        'X-Parse-REST-API-Key': 'API_KEY',
    }

    # Class-Level Operations (CRUD)

    def create_class(self, class_name, data):
        url = f'{self.BASE_URL}{class_name}'
        response = requests.post(url, json=data, headers=self.HEADERS)
        return response.json()

    def read_class(self, class_name):
        url = f'{self.BASE_URL}{class_name}'
        response = requests.get(url, headers=self.HEADERS)
        return response.json()

    def update_class(self, class_name, data):
        url = f'{self.BASE_URL}{class_name}'
        response = requests.put(url, json=data, headers=self.HEADERS)
        return response.json()

    def delete_class(self, class_name):
        url = f'{self.BASE_URL}{class_name}'
        response = requests.delete(url, headers=self.HEADERS)
        return response.json()

    # Object-Level Operations (CRUD)

    def create_object(self, class_name, data):
        url = f'{self.BASE_URL}{class_name}'
        response = requests.post(url, json=data, headers=self.HEADERS)
        return response.json()

    def read_object(self, class_name, object_id):
        url = f'{self.BASE_URL}{class_name}/{object_id}'
        response = requests.get(url, headers=self.HEADERS)
        return response.json()

    def update_object(self, class_name, object_id, data):
        url = f'{self.BASE_URL}{class_name}/{object_id}'
        response = requests.put(url, json=data, headers=self.HEADERS)
        return response.json()

    def delete_object(self, class_name, object_id):
        url = f'{self.BASE_URL}{class_name}/{object_id}'
        response = requests.delete(url, headers=self.HEADERS)
        return response.json()
)
