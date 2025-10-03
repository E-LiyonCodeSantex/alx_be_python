import requests

# Replace with your actual API endpoint and key
url = "http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=Lagos"

response = requests.get(url)
data = response.json()

# Extract and print relevant weather info
temperature = data['current']['temp_c']
description = data['current']['condition']['text']

print(f"Temperature: {temperature}°C")
print(f"Weather: {description}")

