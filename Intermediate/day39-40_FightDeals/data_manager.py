# using sheety API to process data in Google docs
import requests
sheety_endpoint = "https://api.sheety.co/d65ba2aab1558fc6f0e2790b0514e29f/fightDeals/sheet1"
users_endpoint = "https://api.sheety.co/d65ba2aab1558fc6f0e2790b0514e29f/fightDeals/users"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.users_data = {}

    def get_destination_data(self):
        # response = requests.get(url=sheety_endpoint)
        # response.raise_for_status()
        # self.destination_data = response.json()['sheet1']
        self.destination_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 60, 'id': 2},
                                 {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
                                 {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
                                 {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
                                 {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
                                 {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
                                 {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
                                 {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
                                 {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]
        return self.destination_data

    def get_users_data(self):
        # response = requests.get(url=users_endpoint)
        # response.raise_for_status()
        # self.users_data = response.json()['users']
        self.users_data = [{'firstName': 'Jing', 'lastName': 'Lu', 'email': 'jing.lu.cn@outlook.com', 'id': 2},
                           {'firstName': 'Mian', 'lastName': 'Xie', 'email': 'jing.lu.cn@outlook.com', 'id': 3}]
        return self.users_data

    def update_destination_data(self, sheet_data):
        for row in sheet_data:
            new_data = {
                "sheet1": {
                    "iataCode": row["iataCode"],
                }
            }
            put_endpoint = f"{sheety_endpoint}/{row['id']}"
            response = requests.put(url=put_endpoint, json=new_data)
            response.raise_for_status()

    def update_users_data(self, first, last, email):
        new_user = {
            "user": {
                "firstName": first,
                "lastName": last,
                "email": email
            }
        }
        response = requests.post(url=users_endpoint, json=new_user)
        response.raise_for_status()
        print(response.text)
