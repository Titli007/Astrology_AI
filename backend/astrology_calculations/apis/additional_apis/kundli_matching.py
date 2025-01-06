import requests
from dotenv import load_dotenv
import os
# from ...utils.get_user_details import user_detail_fetcher

load_dotenv()

access_token = os.getenv('PROKERALA_ACCESS_TOKEN')


def get_kundli_matching(coordinates, date_time):
    url = f"https://api.prokerala.com/v2/astrology/kundli-matching?ayanamsa=1&girl_coordinates=10.214747%2C78.097626&girl_dob=2004-02-12T15%3A19%3A21%2B05%3A30&boy_coordinates=11.016844%2C76.955832&boy_dob=2000-03-15T10%3A30%3A00%2B05%3A30&la=en"
    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    response = requests.get(url=url, headers=headers)

    print(response.json())

get_kundli_matching('22.615606%2C22.615606','2024-12-26T15%3A30%3A00%2B05%3A30')