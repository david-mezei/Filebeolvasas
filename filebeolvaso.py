# Fájlok beolvasás
autok = []
with open('adatok/autok_listaja.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        auto = {'rendszam': adatok[0], 'tipus': adatok[1], 'kor': int(adatok[2])}
        autok.append(auto)

# print(f'{autok=}')

# for auto in autok:
#     print(f"{auto["rendszam"]} - {auto["tipus"]} - {auto["kor"]}")


"""Legidősebb autó meghatározása"""
legidosebb_auto_kor = autok[0]["kor"]
legidosebb_auto = autok[0]
for auto in autok:
    if auto["kor"] > legidosebb_auto_kor:
        legidosebb_auto_kor = auto["kor"]
        legidosebb_auto = auto

print(f"A legidősebb autó adatai: {legidosebb_auto} ")


"""Legfiatalabb autó meghatározása"""
legfiatalabb_auto_kor = autok[0]["kor"]
legfiatalabb_auto = autok[0]
for auto in autok: 
    if auto["kor"] < legfiatalabb_auto_kor:
        legfiatalabb_auto_kor = auto["kor"]
        legfiatalabb_auto = auto

print(f"A legfiatalabb autó adatai: {legfiatalabb_auto} ")
