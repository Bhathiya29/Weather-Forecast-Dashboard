import requests

# API KEY
API_KEY = '141710af2113bab9f55ef73e1bcd33d5'


def get_data(place, days=None, dataType=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    # Sending the URL in a request to fetch the data
    response = requests.get(url)
    content = response.json()
    # Filtering the returned data by the selected days on the front-end
    filtered_content = content['list']  # weather data is in the list hence first gets this filtered out
    no_values = 8*days
    filtered_content = filtered_content[:no_values]

    # Filtering out by the dataType
    if dataType =='Temperature':
        filtered_content = [dict['main']['temp'] for dict in filtered_content]  # list of all the temperature values
    if dataType =='Sky':
        filtered_content = [dict['weather'][0]['main'] for dict in filtered_content]  # list of all the sky values

    return filtered_content  # This returns the temperature according to the selected no of days


if __name__ == '__main__':
    print(get_data(place='Tokyo',days=3,dataType='Temperature'))
