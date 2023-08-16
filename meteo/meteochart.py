#gemaakt door gino terlingen

#importeren van de nodige elemente

import turtle as t
import http.client as web
import json



#tekenen van y-ass

def draw_yaxis():

    t.pendown()
    t.forward(750)
    t.setheading(270)
    t.forward(750)
    t.setheading(0)
    t.forward(50)
    t.setheading(90)
    t.pendown()



#tekenen van x-ass

def draw_xaxis():
    
    t.pendown()
    t.forward(950)
    t.setheading(180)
    t.forward(950)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.pendown() 



#keuze menu voor de gebruiker

print("hallo welkom bij deze weer grafiek\nkies een land\noptie\nbelgië\nduitsland\nspanje\nengeland\nschotland\nusa")

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
elif stad == ("usa"):
    latitude = 38.90
    longitude = -77.04
else:
    print("dit is geen optie")
    exit()



#initialize api informatie 

landUrl = f'/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m'


conn = web.HTTPSConnection("api.open-meteo.com")
payload = ''
headers = {}
conn.request("GET", landUrl, payload, headers)
res = conn.getresponse()

api = json.loads(res.read())


X = 0
Xschaal = 6
Yschaal = 9



#beging turtle klaar zetten

t.speed(0)
t.left(90) 
t.color('red')
t.penup()
t.setpos(-450,-350)



#loops voor de assen tekenen

for i in range(20):
    draw_yaxis()

t.penup()
t.setpos(-450,-350)
t.setheading(0)

for i in range(15):
    draw_xaxis()



#temperatuur tekenen

O=45
Y=("°C")
H=("verdana",15,"normal")

t.penup()
t.pencolor('black')
t.goto(-510.00,380.00)

for i in range(18):
    t.write(f"{O}{Y}",font=(H))
    t.setheading(270)
    t.forward(43)
    O-=5



#plaatsnaam tekenen

t.goto(0.00,400.00)
t.write(stad.upper(), font=(H))



#lijn van de temperatuur tekenen

t.speed(6)
t.up()
t.pencolor('#0000ff')
t.pensize(10)
Xverschil = 450
for Y in api['hourly']['temperature_2m']:
   t.goto((X * Xschaal)-Xverschil, Y * Yschaal)
   X += 1
   t.down()

t.pencolor('green')
t.penup()
t.goto(-450.00,-380.00)
t.setheading(0)



#datum tekenen

P = api["hourly"]["time"]
K = 0

for i in range(7):
    M = (P[K])
    t.write(M[5:-6],font=(H))
    t.forward(140)
    K+=24



#bericht voor de gebruiker

print("dankjewel tot de volgende keer")

t.done()