import threading
import requests

API_URL = "http://universities.hipolabs.com/search"

def fetch_universities(country, result):
    response = requests.get(API_URL, params={"country": country})
    data = response.json()
    result[country] = [u["name"] for u in data[:20]]


countries = ["Poland", "Germany", "France"]
results = {}
threads = []

for country in countries:
    t = threading.Thread(target=fetch_universities, args=(country, results))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

for country, universities in results.items():
    print(f"\n{country}:")
    for i, name in enumerate(universities, 1):
        print(f"  {i}. {name}")