programnyelvek = []
with open('adatok/Timeline_of_ programming_languages.txt', 'r', encoding='utf-8') as forrasfajl:
    # skippel két sort: 
    for i in range(2):
            next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        programnyelv = {"year": int(adatok[0]), "programming language": adatok[1], "first name": adatok[2], "last name of chief developer": adatok[3]}
        programnyelvek.append(programnyelv)


for programnyelv in programnyelvek:
    print(f"{programnyelv["year"]} - {programnyelv["programming language"]}  - {programnyelv["first name"]} {programnyelv["last name of chief developer"]} ")

print()

"""Legfiatalabb nyelv meghatározása:"""
legf_nyelv_ev = programnyelvek[0]["year"]
legf_nyelv = programnyelvek[0]
for programnyelv in programnyelvek: 
    if programnyelv["year"] < legf_nyelv_ev:
        legf_nyelv_ev = programnyelv["year"]
        legf_nyelv = programnyelv

print(f"A legfiatalabb programozási nyelv adatai: {legf_nyelv} ")

"""Legidősebb nyelv meghatározása:"""
legi_nyelv_ev = programnyelvek[0]["year"]
legi_nyelv = programnyelvek[0]
for programnyelv in programnyelvek: 
    if programnyelv["year"] > legi_nyelv_ev:
        legi_nyelv_ev = programnyelv["year"]
        legi_nyelv = programnyelv

print(f"A legidősebb programozási nyelv adatai: {legi_nyelv} ")
