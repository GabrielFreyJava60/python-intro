import requests
from typing import Optional


def getExchangeRate(codeFrom: str, codeTo: str, api_key: str = "YOUR_API_KEY_HERE") -> Optional[float]:
    try:
        url = f"http://data.fixer.io/api/latest"
        params = {
            "access_key": api_key,
            "base": "EUR",
            "symbols": f"{codeFrom},{codeTo}"
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get("success") and "rates" in data:
                rates = data["rates"]
                
                if codeFrom in rates and codeTo in rates:
                    rate_from = rates[codeFrom]
                    rate_to = rates[codeTo]
                    
                    exchange_rate = rate_to / rate_from
                    return round(exchange_rate, 4)
        
        return None
    except Exception:
        return None


def travelInfoProvider(countryFrom: str, countryTo: str, currencyCodeFrom: str, currencyCodeTo: str, api_key: str = "YOUR_API_KEY_HERE") -> dict:
    exchange_rate = getExchangeRate(currencyCodeFrom, currencyCodeTo, api_key)
    
    return {
        "countryFrom": countryFrom,
        "countryTo": countryTo,
        "currencyCodeFrom": currencyCodeFrom,
        "currencyCodeTo": currencyCodeTo,
        "exchangeRate": exchange_rate
    }
