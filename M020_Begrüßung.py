
# Begrüßung

# Es soll eine Begrüßung in Abhängingkeit zur Uhrzeit ausgegeben werden.

# Zwischen 22Uhr und 5Uhr: Gute Nacht
# Vor 11Uhr: Guten Morgen
# Vor 15Uhr: Mahlzeit
# Vor 18Uhr: Guten Nachmittag
# Vor 22Uhr: Guten Abend

# Benutze zum Testen randint(0, 23),
# um eine Zahl von 0 bis 23 zu erzeugen.

from random import randint

class Greeter:
    def __init__(self):
        self.MORNING = "Guten Morgen"
        self.DAYTIME = "Mahlzeit"
        self.AFTERNOON = "Guten Nachmittag"
        self.EVENING = "Guten Abend"
        self.NIGHT = "Gute Nacht"
        self.greetings = [self.NIGHT, self.MORNING, self.DAYTIME,
                          self.AFTERNOON, self.EVENING]

    def greet(self, hour :int) -> str:
        res = ""
        if hour > 4 and hour < 22:
             if hour < 15:
                 if hour < 11:
                     res = self.MORNING
                 else:
                     res = self.DAYTIME
             else:
                 if hour < 18:
                     res = self.AFTERNOON
                 else:
                     res = self.EVENING
        else:
            res = self.NIGHT

        return res

    def greet2(self, hour :int) -> str:
        night = hour < 4 or hour > 22
        morning = not night and hour < 11
        daytime = not morning and hour < 15
        afternoon = not daytime and hour < 18
        evening = not afternoon

        times = [night, morning, daytime, afternoon, evening]

        return self.greetings[times.index(True)]


if __name__ == '__main__':
    greeter = Greeter()
    for i in range(5):
        hour = randint(0, 23)
        print(hour, " Uhr: ", greeter.greet(hour))
    for j in range(5):
        hour = randint(0, 23)
        print(hour, " Uhr: ", greeter.greet2(hour))
