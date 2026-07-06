import requests
API_key="946c3aceaece8d1ed148450bd79d80da"
base_url=f"https://api.openweathermap.org/data/2.5/weather"
def get_weather(city):
  try:
    url=f"{base_url}?q={city}&appid={API_key}&units=metric"
    response=requests.get(url)
    if response.status_code==200:
      data=response.json()
      weather={
          "City": data["name"],
          "Temperature":f"{data["main"]["temp"]}C",
          "Weather":data["weather"][0]['description'].title(),
          "Humidity":f"{data['main']['humidity']}%",
          "Wind Speed":f"{data['wind']['speed']}m/s"
      }
      return weather
    elif response.status_code==404:
      print("City not found")
      return None
    else:
      print("Failed to fetch weather data")
      return None
  except Exception as e:
    print(f"An error occurred: {e}")
  return None

def display_weather(weather):
    print("\n---Weather Report---")
    for key,value in weather.items():
      print(f"{key}: {value}")

while True:
  print("\n---Weather App---")
  city=input("Enter the city name(or 'exit' to quit): ").strip()
  if city.lower()=='exit':
    print("Thankyou for using!")
    break
  weather=get_weather(city)
  if weather:
    display_weather(weather)
