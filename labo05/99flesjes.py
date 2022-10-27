bottles = 99
while bottles > 0:
    if bottles > 1:
        print (f"{bottles} flesje met bier op de muur, {bottles} flesje met bier. Open er een, drink hem meteen, {bottles - 1} flesje met bier op de muur.")
    elif bottles == 1:
        print (f"{bottles} flesje met bier op de muur, {bottles} flesje met bier. Open er een, drink hem meteen, {bottles - 1} flesje met bier op de muur.")
    bottles -= 1