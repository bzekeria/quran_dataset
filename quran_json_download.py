# load library
import requests

# obtain data
response = requests.get("http://api.alquran.cloud/v1/quran/quran-uthmani")

# return JSON object
data = response.json()

# write to JSON
with open("data/holy_quran.json") as outfile:
    json.dump(data, outfile)
