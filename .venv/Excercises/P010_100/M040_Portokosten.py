
# Portokosten

"""
Die Portokosten (Versandkosten) sind wie folgt festgelegt:
 0 - 39.99 € Bestellwert kosten 3.99 € Porto
40 - 69.99 € Bestellwert kosten 2.99 € Porto
70 - 99.99 € Bestellwert kosten 1.99 € Porto
ab 100 € ist scfrei

Es soll eine Zufallszahl (bestellwert)
von 1.00 - 130.00 erzeugt werden (z.B. 40.47, 123.78)

Dann soll ermittelt werden,
wie hoch die entsprechenden Portokosten sind.
Am Ende sollen der Bestellwert, die Portokosten
und der Gesamtbetrag ausgegeben werden.
"""

class ShippingCostCalculator:
    def calculate(self, price :float) -> float:
        sc = 0
        if price < 100:
            sc = 1.99
            if price < 70:
                sc += 1
                if price < 40:
                    sc +=1
        return sc;

    def cost_info(self, price :float):
        sc = self.calculate(price)
        info = "{:<15}{:>6.2f}€"
        for s in [["Bestellwert", price], ["Portokosten", sc],
                    ["Gesamtbetrag", price + sc]]:
            print(info.format(s[0], s[1]))

if __name__ == '__main__':
    calculator = ShippingCostCalculator()
    calculator.cost_info(56)

