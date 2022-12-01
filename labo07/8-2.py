def panekoek(test, test1):
    pro = 0
    pot = []
    for x in test:
        if x in pot:
            continue
        pot.append(x)
        if x in test1:
            pro = pro+1
    return pro
print( panekoek("appel", "peer"))

            
