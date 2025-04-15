
#  Urlaubsanspruch
#
#  Für die Bestimmung des Urlaubsanspruch der Beschäftigten einer Firma
#  soll ein Programm entwickelt werden.
#  Die Grundlage für die Berechnung des Urlaubsanspruch
#  bildet die Betriebsvereinbarung.
#  Das Programm soll die Anzahl der Urlaubstage für
#  jeweils einen Beschäftigten berechnen.
#
#  Betriebsvereinbarung:
#  Allen Beschäftigten stehen 26 Tage Urlaub zu.
#  Minderjährige Beschäftigte erhalten 30 Tage Urlaub.
#  Beschäftigte, die älter als 55 Jahre sind, erhalten 28 Tage Urlaub.
#  Beschäftigte mit einer Behinderung ab 50 % erhalten
#  zusätzlich 5 weitere Tage Urlaub.
#  Beschäftigte mit einer Betriebszugehörigkeit von mehr als 10 Jahren
#  erhalten 2 zusätzliche Tage Urlaub.

def vacation_entitlement(age :int, seniority :int, challenged=False):
    ve = 26
    if age < 18:
        ve += 4
    if age > 55:
        ve += 2
    if challenged:
        ve += 5
    if seniority > 10:
        ve += 2
    return ve
