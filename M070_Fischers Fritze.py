
# Fischers Fritze

# Es steht folgender String zur Verfügung:
satz = 'Fischers Fritz fischt frische Fische'

# Gib durch String-Slicing des Strings 'satz' die folgenden Strings aus
# 1. ihsrzihf
# 2. sifhrhi
# 3. sche (mit möglichst wenig Zeichen)
# 4. eci hsr hsfziFseci
# 5. ii i

print(satz[1:24:3])
print(satz[7:-1:4])
print(satz[-4:])
print(satz[-1::-2])
print(satz[1::10])
