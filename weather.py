import requests

def Weather(City):
    try:
        city = City
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Couldn't fetch weather info."
    except:
        return "Error getting weather data."