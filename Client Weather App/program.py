import requests
import json


def main():
    # print the header
    print_the_header()
    code = input("what do you want to know for (1920): ")

    # get zipcode from user
    # get Html from web
    weather_data = json.loads(get_html_from_web(code))

    print(weather_data['weather'][0]['main'])
    # parse the html

    # display for the forecast


def print_the_header():
    print('=====================')
    print('     Weather App')
    print('=====================')
    print()


def get_html_from_web(zipcode):
    # need to get Api key from https://openweathermap.org for free.
    url = 'https://samples.openweathermap.org/data/2.5/weather?zip=' + zipcode + ',us&appid=f92437c0ed5556d02728224636972d12'
    response = requests.get(url)
    # print(response.text)
    return response.text


if __name__ == '__main__':
    main()

