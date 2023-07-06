import json
import os
import requests
from dotenv import load_dotenv
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
from geopy.geocoders import Nominatim


def configure():
    load_dotenv()


geolocator = Nominatim(user_agent='myapp')
DATA_URL = "http://api.weatherapi.com/v1"
USER_LOCATION = ""


def get_weather(location):
    url = f"{DATA_URL}/current.json?key={os.getenv('API_KEY')}&q={location}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data


def display_weather(weather_data):
    city = weather_data['location']['name']
    country = weather_data['location']['country']
    temperature = weather_data['current']['temp_f']
    condition = weather_data['current']['condition']['text']

    print(f'Weather in {city}, {country}')
    print(f'Temperature: {temperature}°F')
    print(f'Condition: {condition}')

    # extract the data needed for the user
    # print out the data that was previously extracted


def get_user_location():
    user_location = input("Please enter in your location: ")
    return user_location
    # prompt the user to enter in their location


def validate_user_location(user_location):

    if not user_location:
        print("Location can not be empty.")
        print("Please try again.")
        get_user_location()
        return False
    try:
        location = geolocator.geocode(user_location)
        if location is not None:
            return True
        else:
            return False

    except (GeocoderTimedOut, GeocoderUnavailable) as e:
        print('Geocoding service error: ', str(e))
        return False

    # validate the location that the user has entered in


def main():
    load_dotenv()

    guest_session_bool = True
    print('Hello and welcome to my Py-Weather app')

    while guest_session_bool:
        # step 1: get users location
        guest_location = get_user_location()
        # step 2: validate the entered in location
        validate_user_location(guest_location)
        # step 3: get weather for the users location
        display_weather(get_weather(guest_location))
        # step 4: display the retrieved data from the data source

        print("Would you like to get the weather for another city?")
        guest_answer = input(" Yes or No: ")
        if guest_answer.lower() == "yes":
            guest_session_bool = True
        else: guest_session_bool = False


if __name__ == '__main__':

    main()
