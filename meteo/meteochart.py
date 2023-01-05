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

api = json.loads(res.read())


X = 0
XScale = 5
YScale = 14
t.pencolor('#ff0000')
t.pensize(2)
t.tracer(0, 0)
t.ht()

t.penup()
t.goto(-450.00,400.00)
t.pendown()
t.goto(-450.00,-300.00)
t.goto(500.00,-300.00)
t.penup()
t.goto(-450.00,380.00)
t.pendown()
t.goto(500.00,380.00)
t.penup()
t.goto(-450.00,340.00)
t.pendown()
t.goto(500.00,340.00)
t.penup()
t.goto(-450.00,300.00)
t.pendown()
t.goto(500.00,300.00)
t.penup()
t.goto(-450.00,260.00)
t.pendown()
t.goto(500.00,260.00)
t.penup()
t.goto(-450.00,220.00)
t.pendown()
t.goto(500.00,220.00)
t.penup()
t.goto(-450.00,180.00)
t.pendown()
t.goto(500.00,180.00)
t.penup()
t.goto(-450.00,140.00)
t.pendown()
t.goto(500.00,140.00)
t.penup()
t.goto(-450.00,100.00)
t.pendown()
t.goto(500.00,100.00)
t.penup()
t.goto(-450.00,60.00)
t.pendown()
t.goto(500.00,60.00)
t.penup()
t.goto(-450.00,20.00)
t.pendown()
t.goto(500.00,20.00) 
t.penup()
t.goto(-450.00,-20.00)
t.pendown()
t.goto(500.00,-20.00)
t.penup()
t.goto(-450.00,-60.00)
t.pendown()
t.goto(500.00,-60.00)
t.penup()
t.goto(-450.00,-100.00)
t.pendown()
t.goto(500.00,-100.00)
t.penup()
t.goto(-450.00,-140.00)
t.pendown()
t.goto(500.00,-140.00)
t.penup()
t.goto(-450.00,-180.00)
t.pendown()
t.goto(500.00,-180.00)
t.penup()
t.goto(-450.00,-220.00)
t.pendown()
t.goto(500.00,-220.00)
t.penup()
t.goto(-450.00,-260.00)
t.pendown()
t.goto(500.00,-260.00)
t.penup()

t.pencolor('#000000')
t.goto(-510.00,380.00)
t.write("35°c", font=("verdana",15,"normal"))
t.goto(-510.00,340.00)
t.write("30°c", font=("verdana",15,"normal"))
t.goto(-510.00,300.00)
t.write("25°c", font=("verdana",15,"normal"))
t.goto(-510.00,260.00)
t.write("20°c", font=("verdana",15,"normal"))
t.goto(-510.00,220.00)
t.write("15°c", font=("verdana",15,"normal"))
t.goto(-510.00,180.00)
t.write("10°c", font=("verdana",15,"normal"))
t.goto(-510.00,140.00)
t.write("5°c", font=("verdana",15,"normal"))
t.goto(-510.00,100.00)
t.write("0°c", font=("verdana",15,"normal"))
t.goto(-510.00,60.00)
t.write("-5°c", font=("verdana",15,"normal"))
t.goto(-510.00,20.00)
t.write("-10°c", font=("verdana",15,"normal"))
t.goto(-510.00,-20.00)
t.write("-15°c", font=("verdana",15,"normal"))
t.goto(-510.00,-60.00)
t.write("-20°c", font=("verdana",15,"normal"))
t.goto(-510.00,-100.00)
t.write("-25°c", font=("verdana",15,"normal"))
t.goto(-510.00,-140.00)
t.write("-30°c", font=("verdana",15,"normal"))
t.goto(-510.00,-180.00)
t.write("-35°c", font=("verdana",15,"normal"))
t.goto(-510.00,-220.00)
t.write("-40°c", font=("verdana",15,"normal"))
t.goto(-510.00,-260.00)
t.write("-45°c", font=("verdana",15,"normal"))
t.goto(-510.00,-300.00)
t.write("-50°c", font=("verdana",15,"normal"))

t.goto(0.00,400.00)
t.write(stad.upper(), font=("verdana",15,"normal"))

t.tracer(1, 8)
t.st()




t.speed(2)
t.up()
t.pencolor('#0000ff')
t.pensize(10)
xoffset = 450
for Y in api['hourly']['temperature_2m']:
   t.goto((X * XScale)-xoffset, Y * YScale)
   X += 1
   t.down()
t.done()