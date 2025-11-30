# HW 37 Definition

## Write module tools.py with function getWeather(city) returning string of weather containing the following

1. City name
2. Temperature
3. Condition
4. Humidity
5. Wind speed

### Requirements:

1. Use API of https://www.weatherapi.com/docs/
2. Real time weather data

## Write module weather_integration_test.py containing integration test (not unit test) of using getWeather function call for any existing and not existing city

## Setup

1. Get API key from https://www.weatherapi.com/
2. Set environment variable:
```bash
export WEATHER_API_KEY='your_api_key_here'
```

## Usage

```python
from tools import getWeather

result = getWeather("London")
print(result)
```

## Running Tests

```bash
python3 -m pytest weather_integration_test.py -v
```

or

```bash
python3 weather_integration_test.py
```
