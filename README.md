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

## Architecture

### main.py
Phi-3 chat implementation using Ollama API (localhost:11434)
- Interactive chat with phi-3 model
- Maintains conversation history
- Type 'exit' to quit

### tools.py
Weather API integration module
- `getWeather(city)` function for real-time weather data
- Returns formatted weather information string

### weather_integration_test.py
Interactive integration test
- Allows user to test weather function
- Enter city name to get weather
- Type 'exit' to quit

## Setup

### 1. Install Ollama and phi-3 model
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull phi3
ollama serve
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Start Phi-3 Chat
```bash
python3 main.py
```

### Test Weather Function
```bash
python3 weather_integration_test.py
```

### Use Weather Function in Code
```python
from tools import getWeather
result = getWeather("London")
print(result)
```
