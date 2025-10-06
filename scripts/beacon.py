
import requests, time, random

SERVER = SERVER = "http://<YOUR IP HERE>"   
intervals = [5, 10, 15]

while True:
    headers = {"User-Agent": f"BadBot/{random.randint(1000,9999)}", "X-Client-ID": "id-"+str(random.randint(1000,9999))}
    try:
        r = requests.get(SERVER + "/checkin", headers=headers, timeout=5)
        print("Beacon sent, status:", r.status_code)
    except Exception as e:
        print("Error:", e)
    time.sleep(random.choice(intervals))
