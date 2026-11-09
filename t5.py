# kaisla Miettinen 2523617

class KurssiSuoritus():
    def __init__(self, nimi: str, pisteet: int, arvosana: int):
        self.nimi = nimi
        self.pisteet = pisteet
        self.arvosana = arvosana

    def __repr__(self):
        return f"nimi: {self.nimi}, pisteet: {self.pisteet}, arvosana: {self.arvosana}"
    def __eq__(self, toinen):
        return self.nimi == toinen.nimi and self.pisteet == toinen.pisteet

class SuoritusOte():
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.suoritukset = []

    def __repr__(self):
        return f"{self.nimi}: {self.suoritukset}"

    def lisääSuoritus(self, uusisuoritus: KurssiSuoritus):
        if uusisuoritus in self.suoritukset:
            for suoritus in self.suoritukset:
                if suoritus == uusisuoritus:
                    if uusisuoritus.arvosana > suoritus.arvosana:
                        suoritus.arvosana = uusisuoritus.arvosana
        else:
            self.suoritukset.append(uusisuoritus)

    def opintoPisteet(self):
        summa =0
        for suoritus in self.suoritukset:
            summa += suoritus.pisteet
        return summa
    def keskiarvo(self):
        summa =0
        for suoritus in self.suoritukset:
            summa += suoritus.arvosana
        return summa / len(self.suoritukset)
    def painotettuKeskiarvo(self):
        summa =0
        pisteet =0
        for suoritus in self.suoritukset:
            summa += suoritus.arvosana*suoritus.pisteet
            pisteet+=suoritus.pisteet
        return summa/pisteet

nimi = input("anna nimi: ")
ote = SuoritusOte(nimi)

while True:
    print("Anna kurssin nimi (lopeta lopettaa)")
    nimi = input("anna kurssin nimi: ")

    if nimi== "lopeta":
        break

    pisteet= int(input("anna pisteet: "))
    arvosana = int(input("anna arvosana: "))

    suoritus = KurssiSuoritus(nimi, pisteet, arvosana)
    ote.lisääSuoritus(suoritus)

print(ote)
print("op:", ote.opintoPisteet())
print("ka:", ote.keskiarvo())
print("pka:", ote.painotettuKeskiarvo())