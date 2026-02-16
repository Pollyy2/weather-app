import geocoder
import requests
import json

def get_current_coordinates():
    #getting current location from user IP adress
    g = geocoder.ip('me')
    #list of latitude and longitude
    coordinates = g.latlng

    latitude, longitude = coordinates    
    #URL for reverse geocoding (getting city/country from coordinates)
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"

    headers = {
    "User-Agent": "my_weather_app"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    address = data.get("address", {})

    city = address.get("city") or address.get("town") or address.get("village")
    country = address.get("country")
    filtered_response = {
        "lat": latitude,
        "lon": longitude,
        "city" : city
        
    }

    with open("location.json", "w", encoding="utf-8") as f:
        json.dump(filtered_response, f, ensure_ascii=False, indent=4)

    
    #return all data as a dictionary
    return {
        "latitude": latitude,
        "longitude": longitude,
        "city": city,
        "country": country
    }

print(get_current_coordinates())




