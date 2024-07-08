from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# Load environment variables from a .env file
load_dotenv()

def get_current_weather(city="detroit city"):
    # Construct the API request URL
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    # Make the request and get the response in JSON format
    weather_data = requests.get(request_url).json()
    
    return weather_data

if __name__ == "main_":
  print('\n*** Get Current Weather Conditions ***\n')
city = input("\nPlease enter a city name: ")
if not bool(city.strip()):
  city = "chennai"
weather_data = get_current_weather(city)
print("\n")
print(weather_data)

