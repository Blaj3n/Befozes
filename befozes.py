print("1. feladat")
uvegek = [5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3]
print(uvegek)

print("2. feladat")
osszeslekvar = sum(uvegek)
print(f"Mari néni lekvárja (dl): {osszeslekvar}")

print("3. feladat")
max_szam = 0
pozicio = 0

for i, uveg in enumerate(uvegek):
    if uveg > max_szam:
        max_szam = uveg
        pozicio = i + 1

print(f"A legnagyobb üveg {max_szam} deciliteres és a {pozicio}. a sorban.")

print("4. feladat")

elegendo_uveg = sum(uvegek)
if elegendo_uveg >= osszeslekvar:
    print("Elegendő üveg volt.")
else:
    print("Maradt lekvár.")