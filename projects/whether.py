import requests

def get_weather(city_name, api_key):
    # OpenWeatherMap API URL with city name and API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"

    # Fetching data from OpenWeatherMap API
    response = requests.get(complete_url)

    # Check if the response is valid
    if response.status_code == 200:
        # Parsing JSON data
        data = response.json()
        
        # Extract weather information
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        feels_like = main['feels_like']
        humidity = main['humidity']
        
        # Display weather information
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_desc.capitalize()}")
    else:
        print("City not found or invalid API key.")

# Replace 'your_api_key_here' with your actual API key from OpenWeatherMap
api_key = 'your_api_key_here'
city_name = input("Enter city name: ")
get_weather(city_name, api_key)
