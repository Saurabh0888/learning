import requests
from datetime import datetime

# New function for weekday
# added another comment for testing
def is_weekday():
    today = datetime.today()
    return (0<= today.weekday()<5)

# def get_holidays():
#     r = requests.get('http://localhost/api/holidays')
#     if r.status_code == 200:
#         return r.json()
#     return None


class Holiday():
    def get_holidays(self):
        r = requests.get('http://localhost/api/holidays')
        if r.status_code == 200:
            return r.json()
        return None
