
def oppervlakte_van_driehoek( basis, hoogte ):
    opp = 0.5 * basis * hoogte
    return( "Een driehoek met", basis , "en hoogte", hoogte , "heeft oppervlakte", opp )
   
basis = int(input ("geef je getal"))
hoogte = int(input ("geef je tweede getal"))
print(oppervlakte_van_driehoek(basis, hoogte))