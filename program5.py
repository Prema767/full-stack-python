
import requests

API_KEY = "YOUR_API_KEY"

def get_weather():

    city = input("Enter city name: ")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:

            print("\n===== WEATHER REPORT =====")

            print("City:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Weather:", data["weather"][0]["main"])
            print("Description:", data["weather"][0]["description"])

        else:
            print("City not found or API error!")
            print(data.get("message", ""))

    except requests.exceptions.RequestException:
        print("Connection error! Check your internet.")


def get_forecast():

    city = input("\nEnter city for forecast: ")

    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:

            print("\n===== WEATHER FORECAST =====")

            for item in data["list"][:3]:
                print("Date:", item["dt_txt"])
                print("Temperature:", item["main"]["temp"], "°C")
                print("Weather:", item["weather"][0]["description"])
                print("----------------------")

        else:
            print("Unable to get forecast!")
            print(data.get("message", ""))

    except requests.exceptions.RequestException:
        print("Connection error!")


while True:

    print("\n===== WEATHER APP =====")
    print("1. Current Weather")
    print("2. Weather Forecast")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        get_weather()

    elif choice == "2":
        get_forecast()

    elif choice == "3":
        print("Thank you for using Weather App!")
        break

    else:
        print("Invalid choice! Try again.")
