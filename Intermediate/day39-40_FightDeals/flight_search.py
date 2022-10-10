import requests
from pprint import pprint
from flight_data import FlightData

flight_endpoint = "https://tequila-api.kiwi.com/locations/query"
search_endpoint = "https://tequila-api.kiwi.com/v2/search"
API_KEY = "SNIqMqeMtsc62Ap4LtgVDjdk6ku1IIqT"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        headers = {"apikey": API_KEY}
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=flight_endpoint, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()["locations"]
        code = data[0]["code"]
        print(code)
        return code

    def get_fight_data(self, origin_city_code, destination_city_code, start_date, end_date):

        headers = {
            "apikey": API_KEY,
        }
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": start_date,
            "date_to": end_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }
        response = requests.get(url=search_endpoint, headers=headers, params=params)
        response.raise_for_status()

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_city=data['cityFrom'],
            origin_airport=data['flyFrom'],
            destination_city=data['cityTo'],
            destination_airport=data['flyTo'],
            out_date=data['route'][0]['local_departure'].split("T")[0],
            return_date=data['route'][1]['local_departure'].split("T")[0],
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data


