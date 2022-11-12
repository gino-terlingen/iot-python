producten = ["appel", "banaan", "wortel", "kers", "tomaat"]
prijzen = [0.75, 1.25, 0.25, 0.75, 0.5] 


for index, producten in enumerate(producten):
    print(f"{producten} - €{prijzen[index]}")