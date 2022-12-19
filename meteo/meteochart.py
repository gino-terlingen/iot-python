#gemaakt door gino terlingen

print("hallo welkom bij deze weer grafiek")
print ("kies een stad")
stad = input("we zullen eens kijken voor: ")


if stad == ("antwerpen"):
    latitude = 51.22
    longitude = 4.40
elif  stad == ("brugge"):
    latitude = 51.21
    longitude = 3.22
elif stad == ("oostende"):
    latitude = 51.22
    longitude = 2.93
elif stad == ("brussel"):
    latitude = 50.85
    longitude = 4.35
elif stad == ("luik"):
    latitude = 51.00
    longitude = 3.02         



print  (latitude)

print (longitude)          

import http.client

conn = http.client.HTTPSConnection("api.open-meteo.com")
payload = ''
headers = {}
conn.request("GET", f"/v1/forecast?hourly=temperature_2m&latitude={latitude}&longitude={longitude}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))