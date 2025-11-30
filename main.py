from tools import getWeather


def main():
    cities = ["London", "New York", "Tel Aviv", "NonExistentCity123"]
    
    for city in cities:
        print(f"\n{'='*50}")
        print(f"Weather for: {city}")
        print('='*50)
        result = getWeather(city)
        print(result)


if __name__ == "__main__":
    main()

