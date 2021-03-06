import requests
import json
from openweathermap_raktas import my_openweathermap_key
import csv

ip_list = ['122.35.203.161', '174.217.10.111', '187.121.176.91', '176.114.85.116', '174.59.204.133', '54.209.112.174', '109.185.143.49', '176.114.253.216', '210.171.87.76', '24.169.250.142']

with open('ip_orai.csv', 'w', newline="") as csv_file:
    csvwriter = csv.writer(csv_file)
    csvwriter.writerow(['IP', 'Country', 'City', 'Temp', 'Weather'])

    for ip in ip_list:
        ip_response = requests.get(f"https://freegeoip.app/json/{ip}")
        ip_location = json.loads(ip_response.text)
        country = ip_location['country_name']
        city = ip_location['city']
        print("Country:", country, "City:", city)
        payload = {'appid': my_openweathermap_key, 'q': city, 'units': "metric"}
        weather_response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
        weather_by_ip = json.loads(weather_response.text)
        ip_temp = weather_by_ip['main']['temp']
        ip_weather = weather_by_ip['weather'][0]['main']
        print("Temp:", ip_temp, "Weather:", ip_weather)
        csvwriter.writerow([ip, country, city, ip_temp, ip_weather])


