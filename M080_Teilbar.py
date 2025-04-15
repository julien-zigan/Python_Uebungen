
# Teilbar
#
#  Schreibe ein Skript, das alle Zahlen von 1 bis 100 ausgibt,
#  die durch drei teilbar sind.
#  Hilfsmittel: Schleife, if, Modulo
#
#  Zusatz 1: Gib die Anzahl der Zahlen aus.
#
#  Zusatz 2: Das Programm soll nun alle Zahlen ausgeben,
#            die durch 3 ODER 7 teilbar sind.
#            Gib auch hiervon die Anzahl aus.

res3 = [i for i in range(1, 101) if i % 3 == 0]
print(res3, "Anzahl:",len(res3))
res7 = [i for i in range(1, 101) if i % 3 == 0 or i % 7 == 0]
print(res7, "Anzahl:",len(res7))
