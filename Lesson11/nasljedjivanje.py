class Otac(object):
    def __init__(self,ime,prezime):
        self.ime=ime
        self.prezime=prezime

    def predstavi_se(self):
        print "Moje ime je: "+self.ime+" "+self.prezime


class Sin(Otac):
    def __init__(self,ime,prezime,igracka):
        Otac.__init__(self,ime,prezime)
        self.igracka=igracka


marko =Sin(ime="Marko",prezime="Makic",igracka="autic")
marko.predstavi_se()

Marin=Otac(ime="Marin",prezime="Makic")
print marko.igracka
