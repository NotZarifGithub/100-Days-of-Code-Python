import requests

SHEETY_END = "https://api.sheety.co/b0e8664bcf50ee02e1a5dac12a79f3ab/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_END)
        result = response.json()
        self.destination_data = result["prices"]
        return self.destination_data

    def update_destination_code(self):
        for i in self.destination_data:
            new_data = {"price": {"IATA Code": i["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_END}/{i['id']}", json=new_data)
            print(response.text)
