import requests
from flight_data import FlightData
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "e7Afs-WihjIe6B4VLFndM40hYWt9Pskq"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_iata_code(self, city_name):
        tequila_header = {"apikey": TEQUILA_API_KEY}
        tequila_param = {"term": city_name}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query",
                                headers=tequila_header, params=tequila_param)

        code = response.json()["locations"][0]["code"]
        return code

    def flight_search(self, origin_city_code, destination_city_code, from_time, to_time):
        tequila_header = {"apikey": TEQUILA_API_KEY, }
        tequila_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/search", headers=tequila_header, params=tequila_params)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights available for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
