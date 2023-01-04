#gemaakt door gino terlingen
import turtle as t
import http.client as web
import json

print("hallo welkom bij deze weer grafiek")
print ("kies een land")
print ("optie")
print ("belgië")
print ("duitsland")
print ("spanje")
print ("engeland")
print ("schotland")

stad = input("we zullen eens kijken voor: ")


if stad == ("belgië"):
    latitude = 50.85
    longitude = 4.35
elif  stad == ("duitsland"):
    latitude = 52.52
    longitude = 13.41
elif stad == ("spanje"):
    latitude = 40.42
    longitude = -3.70
elif stad == ("engeland"):
    latitude = 51.51
    longitude = -0.13
elif stad == ("schotland"):
    latitude = 55.87
    longitude = -4.26
else:
    print("dit is geen optie")
    exit()



#print  (latitude)

#print (longitude)          


landUrl = f'/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m'


conn = web.HTTPSConnection("api.open-meteo.com")
payload = ''
headers = {}
conn.request("GET", landUrl, payload, headers)
res = conn.getresponse()

apiJson = json.loads(res.read())


X = 0
XScale = 5
YScale = 14
t.pencolor('#0000ff')
t.pensize(10)

t.up()
xoffset = 500
for Y in apiJson['hourly']['temperature_2m']:
   t.goto((X * XScale)-xoffset, Y * YScale)
   X += 1
   t.down()
t.done()