from tools import getWeather


while True:
    user_input = input("Enter city or 'exit' -->  ")
    if user_input == 'exit':
        break
    print(getWeather(user_input))
