class Osoba(object):
    def __init__(self,ime,prezime,broj,rodendan,email):
        self.ime=ime
        self.prezime = prezime
        self.broj = broj
        self.rodendan = rodendan
        self.email = email

    def predstavi_se(self):
        return "Moje ime je"+ self.ime +" "+ self.prezime

    def koji_je_tvoj_email(self):
        return "moj email je " + self.email

#glavni program

#Objekt pero

pero=Osoba(ime="Pero",prezime="Peric",broj="0987650987654",rodendan="1234",email="pero@gmail.com")
mare=Osoba(ime="Mare",prezime="Peric",broj="0987650987654",rodendan="56789",email="mare@gmail.com")
jura=Osoba(ime="Jura",prezime="Peric",broj="0987650987654",rodendan="34567",email="jura@gmail.com")

popis_zaposlenika = [pero, mare, jura]
for zaposlenik in popis_zaposlenika:
    print zaposlenik.predstavi_se()


