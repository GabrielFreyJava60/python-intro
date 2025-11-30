import os
import requests


def getWeather(city: str) -> str:
    api_key = os.getenv('WEATHER_API_KEY', 'YOUR_API_KEY_HERE')
    base_url = 'http://api.weatherapi.com/v1/current.json'
    
    try:
        params = {
            'key': api_key,
            'q': city,
            'aqi': 'no'
        }
        
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        location = data['location']
        current = data['current']
        
        weather_info = (
            f"City: {location['name']}, {location['country']}\n"
            f"Temperature: {current['temp_c']}°C ({current['temp_f']}°F)\n"
            f"Condition: {current['condition']['text']}\n"
            f"Humidity: {current['humidity']}%\n"
            f"Wind Speed: {current['wind_kph']} km/h ({current['wind_mph']} mph)"
        )
        
        return weather_info
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            return f"Error: City '{city}' not found"
        return f"Error: HTTP {e.response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: Network error - {str(e)}"
    except KeyError as e:
        return f"Error: Unexpected response format - {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

