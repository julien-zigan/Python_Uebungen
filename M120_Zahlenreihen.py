
# Zahlenreihen

# 1. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5
for i in range(1, 6):
    print(i, end=" ")

print()
#alternativ
print([x for x in range(1, 6)])

print()
# 2. Schreibe eine Schleife, die Folgendes ausgibt:
# 100 90 80 70 60 50 40 30 20 10
for i in range(10):
    print((10 - i) * 10 , end=" ")

print()
#alternativ
print([(10 - x) * 10 for x in range(10)])

print()
# 3. Schreibe eine Schleife, die Folgendes ausgibt:1
# 2000 3000 4000 5000 6000
for i in range(2, 7):
    print(int(i * 1E3), end=" ")

print()
#alternativ
print([int(x * 1E3) for x in range(2, 7)])

print()
# 4. Schreibe eine Schleife, die Folgendes ausgibt:
# 2.0 1.5 1.0 0.5 0.0 -0.5 -1.0
for i in range(6):
    print(2 - i / 2, end=" ")

print()
#alternativ
print([2 - i / 2 for i in range(6)])

print()
# 5. Schreibe eine Schleife, die Folgendes ausgibt:
# 13 17 21 25 29
for i in range(5):
    print(13 + i * 4, end=" ")

print()
#alternativ
print([13 + i * 4 for i in range(5)])

print()
# 6. Schreibe eine Schleife, die Folgendes ausgibt:
# 1.0 2.2 3.4 4.6 5.8 7.0 8.2 9.4
for i in range(8):
    print(1 + i * 1.2, end=" ")

print()
#alternativ
print([x * 1.2 + 1 for x in range(8)])

print()
# 7. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5 6 8 9 10
for i in range(10):
    print(i + 1, end=" ")

print()
#alternativ
print([x + 1 for x in range(10)])

print()
# 8. Schreibe eine Schleife, die Folgendes ausgibt:
# 13 17 21 29 33 37 45
x = 5
for i in range(7):
     x += 8 if not i % 3 else 4
     print(x , end=" ")

print()
print([])
print()
# 9. Schreibe eine Schleife, die Folgendes ausgibt:
# Z5 Z7 Z9 Z11 Z13
for i in range(5):
    print("Z", 5 + i * 2, sep="", end=" ")

print()
#alternativ
print(["Z{}".format(x * 2 + 5) for x in range(5)])

print()
# 10. Schreibe eine Schleife, die Folgendes ausgibt:
# a2b3 a12b13 a22b23
for i in range(3):
    fill = str(i) if i else ""
    print("a", fill, 2, "b", fill, 3,  sep="", end=" ")

print()
#alternativ
print(["a{0}2b{1}3".format((x if x else ""), (x if x else "")) for x in range(3)])

print()
# 11. Schreibe eine Schleife,
# die alle Zahlen von 1 bis 20 addiert
# und danach das Endergebnis ausgibt.
x = 0
for i in range(20):
    x += i + 1
print(x)

print([])
print()
# 12. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5 4 3 2 1
x = 0
for i in range(9):
    x += 1 if i < 5 else -1;
    print(x , end=" ")

print()
print([])