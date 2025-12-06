import requests
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def getExchangeRate(codeFrom: str, codeTo: str, api_key: str = "YOUR_API_KEY_HERE") -> Optional[float]:
    if not all([codeFrom, codeTo, len(codeFrom) == 3, len(codeTo) == 3]):
        logger.warning(f"Invalid currency codes: {codeFrom}, {codeTo}")
        return None
    
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
                else:
                    logger.error(f"Currency codes not found in rates: {codeFrom}, {codeTo}")
            else:
                logger.error(f"API response error: {data.get('error', 'Unknown error')}")
        else:
            logger.error(f"HTTP error: {response.status_code}")
        
        return None
    except requests.RequestException as e:
        logger.error(f"API request failed: {e}")
        return None
    except (KeyError, ZeroDivisionError) as e:
        logger.error(f"Calculation error: {e}")
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
