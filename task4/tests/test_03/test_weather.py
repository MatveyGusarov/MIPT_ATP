import unittest
import pytest
from requests_mock import Mocker
from weather_03.weather_wrapper import BASE_URL, FORECAST_URL, WeatherWrapper

KEY = '197fc3253b8cedb3fa5f3bb170577c51'

weather = WeatherWrapper(KEY)

def test_all(requests_mock):       
    requests_mock.get(BASE_URL, status_code=200, json={'main': {'temp': 0}})
    requests_mock.get(FORECAST_URL, status_code=200, json={'list': [{'main': {'temp': 0}}] * 8})

    assert weather.get_tomorrow_diff('Barcelona') == 'The weather in Barcelona tomorrow will be warmer than today'

    requests_mock.get(FORECAST_URL, status_code=200, json={'list': [{'main': {'temp': 2}}] * 8})
    assert weather.get_tomorrow_diff('Tomsk') == 'The weather in Tomsk tomorrow will be much warmer than today'

    requests_mock.get(FORECAST_URL, status_code=200, json={"list": [{'main': {'temp': -2}}] * 8})
    assert weather.get_tomorrow_diff('Kiev') == 'The weather in Kiev tomorrow will be colder than today'

    assert weather.find_diff_two_cities('Barcelona', 'Astana') > 0
    assert weather.get_diff_string('Barcelona', 'Astana') == 'Weather in Barcelona is warmer than in Astana by 6 degrees'
    
class WeatherTests(unittest.TestCase):
    def test_get_response_city(self, requests_mock):
        requests_mock.get(BASE_URL, status_code=404)
        self.assertRaises(AttributeError, weather.get_response_city, 'Abracadabracity', BASE_URL)
                                                                                                                        