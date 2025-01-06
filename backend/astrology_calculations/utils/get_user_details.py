import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GEOAPIFY_API_KEY')

def get_cordinates(address):
    url=f"https://api.geoapify.com/v1/geocode/search?text={address}&format=json&apiKey={api_key}"
    
    response = requests.get(url)

    data = response.json()

    # print(data)

    lon = data['results'][0]['lon']
    lat = lon = data['results'][0]['lat']

    timezone_offset = data['results'][0]['timezone']['offset_STD']

    result = {"lon" : lon , "lat" : lat, "timezone_offset" : timezone_offset}

    print(result)

    return result


def date_time_formatter(dob, tob, offset):
    date_time = str(dob) + " " + str(tob)
    # Convert to ISO 8601 format manually
    iso_format = date_time.replace(" ", "T") + offset

    # Manually encode the special characters
    encoded_time = iso_format.replace(":", "%3A").replace("+", "%2B")

    print(encoded_time)

    return encoded_time



def user_detail_fetcher(person='user', gender=None, location=None, dob= None, tob= None):
    result = get_cordinates(location)
    coordinates = str(result['lat']) + '%2C' + str(result['lon'])
    offset = result['timezone_offset']

    date_time = date_time_formatter(dob, tob, offset=offset)

    print(coordinates, date_time)

    return {
        "person" : person,
        "gender" : gender,
        "coordinates" : coordinates,
        "date_time" : date_time
    }

# gender, datetime, address

sf = user_detail_fetcher("partner", "female" ,"howrah+westbengal+india", "2024-12-26", "15:30:00")
print(sf)