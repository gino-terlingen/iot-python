def maketitle(title, onder = '='): 
    lengte = len(title)
    tt =  onder*lengte
    return title+"\n"+tt

def printtitle(case):
    title = maketitle("tears of a clown")
    if case == "title":
        title = title.title()
    elif case == "upper":
        title = title.upper()
    print (title)

printtitle(case="title")
printtitle(case="upper")