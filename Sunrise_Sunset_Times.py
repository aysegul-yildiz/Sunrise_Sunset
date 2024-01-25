import requests

latitude = input("Enter the latitude of your locaiton: ")
longitude = input("Enter the longtitude of your location: ")
parameters = {"lat": latitude, "lng": longitude, "formatted":0}
response = requests.get(url="https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()
data_json = response.json()
sunrise = data_json["results"]["sunrise"]
sunset = data_json["results"]["sunset"]
print(f"Sunrise time for your location: {(sunrise.split('T')[1].split(':')[0])}:{(sunrise.split('T')[1].split(':')[1])}\nSunset time for your location: {(sunset.split('T')[1].split(':')[0])}:{(sunset.split('T')[1].split(':')[1])}")
