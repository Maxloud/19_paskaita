import calendar

def is_leep_year(nuo, iki):
    keliamieji = []
    for metai in range(nuo, iki):
        if calendar.isleap(metai):
            keliamieji.append(metai)
    return keliamieji

nuo1 = int(input("iveskite pradzios metus:"))
iki1 = int(input("Iveskite pabaigos metus:"))

print(is_leep_year(nuo1,iki1))
