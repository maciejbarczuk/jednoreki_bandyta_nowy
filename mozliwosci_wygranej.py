
wygrana = [["$", "$", "$"], ["#", "#", "#"], ["@", "@", "@"]]

def polowiczna_wygrana(znak_1, znak_2, znak_3):
    if znak_1 == znak_2 and znak_1 != "-" and znak_2 != "-":
        return True
    elif znak_2 == znak_3 and znak_2 != "-" and znak_3 != "-":
        return True
