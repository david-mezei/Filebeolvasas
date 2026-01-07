programnyelvek = []
with open('adatok/Timeline_of_ programming_languages.txt', 'r', encoding='utf-8') as forrasfajl:
    # skippel két sort: 
    for i in range(2):
            next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(";")
        year = int(adatok[0])
        language = adatok[1]
        first_name = adatok[2]
        last_name = adatok[3]
        programnyelvek.append([year, language, first_name, last_name])

for programnyelv in programnyelvek:
    print(f"{programnyelv[0]} - {programnyelv[1]}  - {programnyelv[2]} {programnyelv[3]} ")

print()

"""Legfiatalabb nyelv meghatározása:"""
legf_nyelv_ev = programnyelvek[0][0]
legf_nyelv = programnyelvek[0]
for programnyelv in programnyelvek: 
    if programnyelv[0] < legf_nyelv_ev:
        legf_nyelv_ev = programnyelv[0]
        legf_nyelv = programnyelv

print(f"A legfiatalabb programozási nyelv adatai: {legf_nyelv} ")

"""Legidősebb nyelv meghatározása:"""
legi_nyelv_ev = programnyelvek[0][0]
legi_nyelv = programnyelvek[0]
for programnyelv in programnyelvek: 
    if programnyelv[0] > legi_nyelv_ev:
        legi_nyelv_ev = programnyelv[0]
        legi_nyelv = programnyelv

print(f"A legidősebb programozási nyelv adatai: {legi_nyelv} ")
