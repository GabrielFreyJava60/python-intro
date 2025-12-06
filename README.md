# HW 39 Definition

## Update function travelInfoProvider

### 1. Extract Lines 11-19 to one function extractJSON
- extractJSON should be universal function taking list of some ordered properties that should be in JSON
- For example, extractJSON(text:str, properties: list[str])->dict for extracting JSON presenting tool call
- extractJSON(text, ["tool", "arguments"]) for extracting tool calls
- extractJSON(text, ["country", "currency_code"]) for extracting currency code value

### 2. Write additional functions for getting exchange rate
- Function to get exchange rate from codeFrom (currency code of the country from) to codeTo (currency code of the country to)
- Use the fixer.io API (The most popular currency rates API) with free access key
- API endpoint: http://data.fixer.io/api/latest?access_key=<API key>

### 3. Fill property exchangeRate
- Fill property exchangeRate with proper value received from function #2

## Usage

### Start Phi-3 Agent
```bash
python3 main.py
```

### Example Interactions

**Weather Query:**
```
You: What is the weather in London?
Agent:  Weather in London(United Kingdom): temperature is 10.5°C...
```

**LTR Evaluation:**
```
You: Calculate (3 + 2) * 10
Agent:  50.0
```

```
You: Evaluate 2 ** 3 + 5
Agent:  13.0
```

**Travel Info Query:**
```
You: Get travel info from USA to France
Agent:  {'countryFrom': 'USA', 'countryTo': 'France', 'currencyCodeFrom': 'USD', 'currencyCodeTo': 'EUR', 'exchangeRate': 0.92}
```

## Files

- `main.py` - Phi-3 chat agent with tool routing and universal extractJSON function
- `tools.py` - Available tools (getWeather, ltrEval, travelInfoProvider)
- `travel_info.py` - Travel info provider with currency exchange (HW#39)
- `system_content.py` - System prompt with tool rules
- `thinking_dots.py` - Loading animation
- `ltr_evaluation.py` - LTR expression evaluator from HW#36
- `weather_integration_test.py` - Weather function test
- `travel_info_test.py` - Travel info functionality test

## Requirements

- Ollama with phi3 model running on localhost:11434
- Python 3.10+
- requests library
