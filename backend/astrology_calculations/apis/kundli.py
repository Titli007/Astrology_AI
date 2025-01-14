import requests
from dotenv import load_dotenv
import os
from astrology_calculations.utils.get_user_details import user_detail_fetcher  # Use absolute import


load_dotenv()

access_token = os.getenv('PROKERALA_ACCESS_TOKEN')


def get_detailed_kundli(coordinates, date_time):
    url = f"https://api.prokerala.com/v2/astrology/kundli?ayanamsa=1&coordinates={coordinates}&datetime={date_time}&la=en"
    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    response = requests.get(url=url, headers=headers)

    print("========================/////////////////////////////////////////",response.json())

    return response.json()

# get_detailed_kundli('22.615606%2C22.615606','2024-12-26T15%3A30%3A00%2B05%3A30')


def kundli_creator(person, gender, location, dob, tob) : 
    user_details = user_detail_fetcher(person , gender, location, dob, tob) 
    kundli_result = get_detailed_kundli(user_details['coordinates'], user_details['date_time'])
    print("kundli_result======================================",kundli_result)
    return kundli_result

# kundli_creator("user","female" ,"howrah+westbengal+india", "2024-12-26", "15:30:00") #"user","female" ,"howrah+westbengal+india", "2024-12-26", "15:30:00"