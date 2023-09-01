# Maak een eenvoudige todo list die alles in geheugen bijhoudt en dus niets
# op disk schrijft.
# Je programma print telkens de mogelijke commando's (zie zo meteen) en de
# lijst van todo-items en vraagt dan wat de gebruiker wil doen. De gebruiker
# antwoordt ofwel met een letter voor een commando, ofwel met een getal, dat
# één van de todo items aanduidt.
# Commando 'a' → Vraag aan de gebruiker een item om toe te voegen.
# Commando 'r' → Laat het programma een willekeurig item uit de lijst kiezen en
#                laat de gebruiker dit uitvoeren. (Zie verderop bij uitvoeren.)
# Commando 'x' → Exit. Als de todo lijst niet leeg is, moet je programma aan de
#                gebruiker eerst bevestiging vragen.
#
# Uitvoeren → Als de gebruiker een getal heeft ingegeven of een willekeurig item
#             heeft laten kiezen, print je programma het item en wacht tot de
#             gebruiker hiermee klaar is. Dit kan hij aangeven door enter te
#             drukken, waarna het item wordt verwijderd. Als hij de taak toch
#             uitvoert, kan hij annuleren met ctrl-c.

# Een voorbeeld sessie van dit programma vind je in todo-example.txt. De input
# van de gebruiker begint hier telkens met een enkel groter-dan-teken (>).

# Belangrijk in deze oefening is:
# * voorkomen dat je code dubbel schrijft; maak gebruik van loops, functies, ...
# * opvangen van foutieve input en andere uitzonderingen
