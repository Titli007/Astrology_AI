import requests
from dotenv import load_dotenv, set_key
import os
import schedule
import time
from pathlib import Path

load_dotenv()

root_dir = Path(__file__).parent.parent.parent
env_path = os.path.join(root_dir, '.env')


def get_access_token():
    print(os.getenv('PROKERALA_CLIENT_SECRET'))
    print(os.getenv('PROKERALA_CLIENT_ID'))
    url = 'https://api.prokerala.com/token'

    # Construct the data as a URL-encoded string (mimicking the raw request)
    data = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('PROKERALA_CLIENT_ID'),
        'client_secret': os.getenv('PROKERALA_CLIENT_SECRET')
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'api.prokerala.com',  # This will explicitly set the host header
    }

    response = requests.post(url=url, headers=headers, data=data)


    if response.status_code == 200:
        access_token = response.json().get('access_token')
        if access_token:
            set_key(env_path,'PROKERALA_ACCESS_TOKEN', access_token)
            print("Access token updated created successfully")
            return access_token
        else:
            print("Access token not found in the response.")
    else:
        print(f"Failed to fetch token: {response.json()}")
        return None
    


get_access_token()

schedule.every(3).hours.do(get_access_token)

# Keep the script running to execute the scheduled task
while True:
    schedule.run_pending()
    time.sleep(1)
