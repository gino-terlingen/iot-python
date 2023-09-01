# Schrijf een functie om 5-puntige sterren te tekenen met behulp van turtle.
# De eerste parameter van je functie is de turtle zelf waarmee je gaat tekenen.
# De volgende parameters hebben telkens een standaard waarde en zijn dus
# optioneel. Dit zijn:
#   pos → de absolute positie waar de ster moet getekend worden. Standaard is
#         deze None wat wil zeggen dat je tekent waar de turtle zich momenteel
#         bevindt. Anders is dit een tuple van coördinaten (bijvb (60, -70))
#   size → de lengte van de zijden van de ster, een goede standaardwaarde is 75.
#   color → de kleur waarin de ster wordt getekend. Als deze None is (standaard),
#           gebruik je de huidige pencolor van de turtle
#   rotate → Het aantal graden dat de turtle draait (naar links of rechts, dit
#            mag je kiezen) voor je tekent, dus de draaiing van de ster.
#
# Een 5-puntige ster kan je tekenen door 5 gelijke lijnen te tekenen en na elke
# lijn 144 graden te draaien. Een voorbeeld vind je hieronder als comments en
# het resultaat ervan in bijlage.

import turtle as t
import random



# Definieer hier je functie drawstar.
def drawstar():
    t.setheading(random.randint(0, 360))
    t.color('black', random.choice(col) )
    t.begin_fill()
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()
    t.forward(75)
    t.right(144)
    t.forward(75)
    t.right(144)
    t.forward(75)
    t.right(144)
    t.forward(75)
    t.right(144)
    t.forward(75)
    t.right(144)
    t.end_fill()


#lijst met kleuren
col = ['red', 'blue', 'black', 'green', 'yellow']



#speed turtle
t.speed(10)

#loop voor def uit te voeren
for i in range(10):
    drawstar() 

t.done()
