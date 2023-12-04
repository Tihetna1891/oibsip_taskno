import requests

def get_weather(api_key, location):
    base_url = "https://www.weatherapi.com/my/"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None
    except requests.ConnectionError:
        print("Error: Unable to connect to the weather API.")
        return None

def display_weather(weather_data):
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_condition = weather_data['weather'][0]['description']

        print(f"\nWeather Information for {weather_data['name']}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Condition: {weather_condition}")
    else:
        print("Unable to fetch weather data.")

def main():
    api_key = 'fd0de36b1f1b4e92bf8160309230911'  # Replace with your OpenWeatherMap API key
    location = input("Enter city or ZIP code: ")

    weather_data = get_weather(api_key, location)

    display_weather(weather_data)

if __name__ == "__main__":
    main()
