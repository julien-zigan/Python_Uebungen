
# Hundealter

# Hundeliebhaber stellen sich häufig die Frage,
# wie alt ihr Hund wohl wäre, wenn er kein Hund, sondern ein Mensch wäre.
# Landläufig rechnet man Hundejahre in Menschenjahre um,
# indem man das Alter des Hundes mit 7 multipliziert.
# Je nach Hundegröße und Rasse sieht die Umrechnung jedoch etwas komplizierter aus,
# z.B.:
# - Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
# - 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
# - Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.

# Schreibe ein Programm, das das Alter eines Hundes erfragt und dann nach obiger
# Methode berechnet, welchem Alter in Menschenjahren das entspricht.

def man_2_dog_years(years :int) -> int:
    if years:
        years = years * 5 + 9
        if years > 14:
            years += 3
    return years

if __name__ == '__main__':
    man_years = int(input("Geben Sie das Alter Ihres Hundes in Menschenjahren ein: "))
    print("Das macht", man_2_dog_years(man_years), "Hundejahre!")
