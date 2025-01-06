import requests
from dotenv import load_dotenv
import os
# from ..utils.get_user_details import user_detail_fetcher

load_dotenv()

access_token = os.getenv('PROKERALA_ACCESS_TOKEN')


def get_detailed_kundli(coordinates, date_time):
    url = f"https://api.prokerala.com/v2/astrology/kundli?ayanamsa=1&coordinates={coordinates}&datetime={date_time}&la=en"
    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    response = requests.get(url=url, headers=headers)

    print(response.json())

get_detailed_kundli('22.615606%2C22.615606','2024-12-26T15%3A30%3A00%2B05%3A30')