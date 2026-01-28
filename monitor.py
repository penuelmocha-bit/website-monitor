import requests
from datetime import datetime

URL = "https://google.com"

def check_website():
    try:
        response = requests.get(URL, timeout=5)

        if response.status_code == 200:
            status = "UP"
        else:
            status = "DOWN"

    except:
        status = "DOWN"

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"{time} - {URL} - {status}"

    print(log)

    with open("status.log", "a") as file:
        file.write(log + "\n")

check_website()