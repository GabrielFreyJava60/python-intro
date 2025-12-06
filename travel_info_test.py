#!/usr/bin/env python3

from travel_info import getExchangeRate, travelInfoProvider
from main import extractJSON


def test_extractJSON():
    print("Testing extractJSON...")
    
    text1 = 'The data is {"tool": "getWeather", "arguments": {"city": "London"}}'
    result1 = extractJSON(text1, ["tool", "arguments"])
    print(f"Test 1: {result1}")
    
    text2 = 'Country info: {"country": "USA", "currency_code": "USD"}'
    result2 = extractJSON(text2, ["country", "currency_code"])
    print(f"Test 2: {result2}")
    
    print()


def test_getExchangeRate():
    print("Testing getExchangeRate...")
    print("Note: This requires a valid API key from fixer.io")
    
    rate = getExchangeRate("USD", "EUR", "YOUR_API_KEY_HERE")
    print(f"Exchange rate USD to EUR: {rate}")
    
    print()


def test_travelInfoProvider():
    print("Testing travelInfoProvider...")
    
    result = travelInfoProvider("USA", "France", "USD", "EUR", "YOUR_API_KEY_HERE")
    print(f"Travel info: {result}")
    
    print()


if __name__ == "__main__":
    test_extractJSON()
    test_getExchangeRate()
    test_travelInfoProvider()
