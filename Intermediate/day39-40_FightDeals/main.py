# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import requests
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()
# Todo: 1,Get the IATA Codes using the Kiwi Partners API and fill in Google sheet
# for row in sheet_data:
#     if row["iataCode"] == "":
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
# data_manager.update_destination_data(sheet_data)

# Todo: 2,Add users' data
add_users = None
ask1 = input("Do you want to add users? (yes/no)\n").lower()
if ask1 == "yes":
    add_users = True
while add_users:
    print("Welcome to Jenny's Flight Club\n"
          "We find the best flight deals and email you")
    first_name = input("What is your first name?\n").capitalize()
    last_name = input("What is your last name?\n").capitalize()
    check_email_input = True
    while check_email_input:
        email = input("What is your email?\n")
        email_again = input("Type your email again.\n")
        if email == email_again:
            data_manager.update_users_data(first_name, last_name, email)
            print("You're in the club!")
            check_email_input = False
        else:
            print("Email is wrong, please type again")
    ask2 = input("Do you want to add another users? (yes/no)\n").lower()
    if ask2 == "no":
        add_users = False

# Todo: 3,Search for Cheap Flights
tomorrow = datetime.today().date() - timedelta(days=-1)
start_date = tomorrow.strftime("%d/%m/%Y")
six_after = datetime.today().date() - timedelta(days=-6 * 30)
end_date = six_after.strftime("%d/%m/%Y")

users_data = data_manager.get_users_data()
print(users_data)

for row in sheet_data:
    flight = flight_search.get_fight_data(
        origin_city_code="LON",
        destination_city_code=row["iataCode"],
        start_date=start_date,
        end_date=end_date
    )
    try:
        if flight.price <= row["lowestPrice"]:
            message = f"Low price alert! Only £{flight.price} to fly " \
                      f"from {flight.origin_city}-{flight.origin_airport} " \
                      f"to {flight.destination_city}-{flight.destination_airport} , " \
                      f"from {flight.out_date} to {flight.return_date}."
            # notification_manager.send_message(text=message)
            for user in users_data:
                name = user['firstName']
                email = user['email']
                notification_manager.send_email(name, email, message)
        else:
            print("No Good Flight Deal")
    except AttributeError:
        pass
