# nama : Hisyam Rosadi
# NIM  : 26241010

a=int(input("digit A: "))
b=int(input("digit B: "))

kondisi1 = a >= 1
kondisi2 = b >= 0

print("digit A: {a}")
print("digit B: {b}")
print(f"kondisi 1: {kondisi1}")
print(f"kondisi 2: {kondisi2}")
print(f"NOT: {not kondisi1}")
print(f"AND: {kondisi1 and kondisi2}")
print(f"OR: {kondisi1 or kondisi2}")
print(f"XOR: {kondisi1 ^ kondisi2}")
#OR :kalau ada 1 ygtrue. boleg dua-duanya
#XOR :cuma true kalok beda.kalok sama-sama true hasilnya false