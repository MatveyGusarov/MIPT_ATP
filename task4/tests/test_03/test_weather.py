import unittest
from requests_mock import Mocker
from weather_03.weather_wrapper import BASE_URL, FORECAST_URL, WeatherWrapper

KEY = '197fc3253b8cedb3fa5f3bb170577c51'

request = Mocker()
weather = WeatherWrapper(KEY)

def test_all():       
    request.get(BASE_URL, status_code=200, json={'main': {'temp': 0}})
    request.get(FORECAST_URL, status_code=200, json={'list': [{'main': {'temp': 0}}] * 8})

    assert weather.get_tomorrow_diff('Barcelona') == 'The weather in Barcelona tomorrow will be warmer than today'

    request.get(FORECAST_URL, status_code=200, json={'list': [{'main': {'temp': 2}}] * 8})
    assert weather.get_tomorrow_diff('Tomsk') == 'The weather in Tomsk tomorrow will be much warmer than today'

    request.get(FORECAST_URL, status_code=200, json={"list": [{'main': {'temp': -2}}] * 8})

    assert weather.find_diff_two_cities('Barcelona', 'Astana') > 0
    assert weather.get_diff_string('Barcelona', 'Astana') == 'Weather in Barcelona is warmer than in Astana by 5 degrees'
    
    request.get(BASE_URL, status_code=404)
    assertRaises(AttributeError, weather.get_response_city, 'Abracadabracity', BASE_URL)
                                                                                                                        
