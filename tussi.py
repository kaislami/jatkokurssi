class Tussi :
    def __init__(self, vari:str):
        self.vari = vari
        self.mustemaara = 5
        self.korkkipaalla = True
    def korkkikiinni(self):
        self.korkkipaalla = True
    def __repr__(self):
        return f"{self.vari}, {self.mustemaara}, {self.korkkipaalla}"
    def korkkiauki(self):
        self.korkkipaalla = False
    def piirra(self):
        if not self.korkkipaalla and self.mustemaara > 0:
            print(f"piirrän {self.vari}")
            print("en piirrä")
            return False

tussi = Tussi("pinkki")
print(tussi)
tussi.korkkiauki()
print(tussi)

tussi.piirra()
print(tussi)
tussi.piirra()
tussi.piirra()
tussi.piirra()
tussi.piirra()
tussi.piirra()