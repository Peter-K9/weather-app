import json
import os



DATA_URL = "http://api.weatherapi.com/v1"
USER_LOCATION = ""

def get_weather(location):
    url = f"{DATA_URL}/current.json?key={API_KEY}&q={location}"


def display_weather(weather_data):
    return
    # extract the data needed for the user
    # print out the data that was previously extracted


def get_user_location():
    user_location = input("What is you location? ")
    return user_location
    # prompt the user to enter in their location


def validate_user_location(user_location):
    return
    # validate the location that the user has entered in


def main():
    print()
    # step 1: get users location
    # step 2: validate the entered in location
    # step 3: get weather for the users location
    # steo 4: display the retieved data from the data source


if __name__ == '__main__':

    main()
