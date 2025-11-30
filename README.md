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

### Phi-3 Chat Installation (macOS)

Phi-3 model is already installed! ✅

**Location:** `~/Downloads/Ollama.app`
**Model:** phi3:latest (2.2 GB)
**Status:** Running on localhost:11434

### Start Ollama Server

```bash
./start_ollama.sh
```

Or manually:
```bash
~/Downloads/Ollama.app/Contents/Resources/ollama serve &
```

### Install Python dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Start Phi-3 Chat
```bash
python3 main.py
```

Example:
```
Phi-3 simple chat. Type 'exit' for quit
You: Привет!
Agent:  Здравствуйте!
____________________________________________________________
You: exit
bye
```

### Test Weather Function
```bash
python3 weather_integration_test.py
```

Example:
```
Enter city or 'exit' -->  London
Weather in London(United Kingdom): temperature is 10.5°C , Partly cloudy,
        speed of wind: 15.2 kph, Humidity is 75%
Enter city or 'exit' -->  exit
```

### Use Weather Function in Code
```python
from tools import getWeather
result = getWeather("London")
print(result)
```

## Verify Installation

Check Ollama status:
```bash
~/Downloads/Ollama.app/Contents/Resources/ollama list
```

Expected output:
```
NAME           ID              SIZE      MODIFIED       
phi3:latest    4f2222927938    2.2 GB    49 seconds ago
```

## Notes

- Ollama server runs on `http://localhost:11434`
- Phi-3 model size: 2.2 GB
- Weather API key is included in tools.py
