import unittest
from tools import getWeather


class TestWeatherIntegration(unittest.TestCase):
    
    def test_existing_city(self):
        result = getWeather("London")
        self.assertIn("City:", result)
        self.assertIn("Temperature:", result)
        self.assertIn("Condition:", result)
        self.assertIn("Humidity:", result)
        self.assertIn("Wind Speed:", result)
        self.assertIn("London", result)
    
    def test_another_existing_city(self):
        result = getWeather("New York")
        self.assertIn("City:", result)
        self.assertIn("Temperature:", result)
        self.assertIn("Condition:", result)
        self.assertIn("Humidity:", result)
        self.assertIn("Wind Speed:", result)
        self.assertIn("New York", result)
    
    def test_city_with_special_characters(self):
        result = getWeather("Tel Aviv")
        self.assertIn("City:", result)
        self.assertIn("Temperature:", result)
        self.assertIn("Israel", result)
    
    def test_non_existing_city(self):
        result = getWeather("NonExistentCityXYZ123")
        self.assertIn("Error:", result)
        self.assertIn("not found", result.lower())
    
    def test_empty_city_name(self):
        result = getWeather("")
        self.assertIn("Error:", result)
    
    def test_invalid_city_name(self):
        result = getWeather("12345!@#$%")
        self.assertIn("Error:", result)
    
    def test_weather_data_format(self):
        result = getWeather("Paris")
        lines = result.split('\n')
        self.assertEqual(len(lines), 5)
        self.assertTrue(lines[0].startswith("City:"))
        self.assertTrue(lines[1].startswith("Temperature:"))
        self.assertTrue(lines[2].startswith("Condition:"))
        self.assertTrue(lines[3].startswith("Humidity:"))
        self.assertTrue(lines[4].startswith("Wind Speed:"))


if __name__ == '__main__':
    unittest.main()

