import requests
from datetime import datetime
import time

print("Program started")

url = input("Enter website URL: ")

def check_website():
    print("Checking website...")

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            status = "UP"
        else:
            status = "DOWN"

    except:
        status = "DOWN"

    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"{time_now} - {url} - {status}"

    print(log)

    with open("status.log", "a") as file:
        file.write(log + "\n")

while True:
    check_website()
    time.sleep(5)