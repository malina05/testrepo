print "Dobro dosli u program za upravljenje zadacima"
popis_zadataka = {}

while True:
    zadatak = raw_input("Molimo upisite zadatak:")
    status =raw_input("Da li je zadatak napravljen? da/ne")
    print "Tvoj zadatak je"+zadatak
    #Kljucni dio
    #vrijedi za liste:
    #lista_zadataka.append(zadatak)

    #vrijedi za rjecnik:
    if status =="da":
        popis_zadataka[zadatak]=True
    else:
        popis_zadataka[zadatak]=False

    novi_zadatak =raw_input("Zelis li upisati novi zadatak da ili ne:")

    if novi_zadatak =="ne":
        break

print "Svi napravljeni zadaci %s" % popis_zadataka

datoteka_zadataka =open("popis_zadataka.txt","w+")
datoteka_zadataka.write("Svi napravljeni zadaci:\n")


for podatak in popis_zadataka:
    if popis_zadataka[podatak] is True:
        print "+"+podatak
        datoteka_zadataka.write("+"+podatak+"\n")

    elif popis_zadataka[podatak] is False:
        print "-"+podatak
        datoteka_zadataka.write("-"+podatak+"\n")
#for podatak in lista_zadataka:
 #   print podatak
datoteka_zadataka.close()

print "Kraj programa!"
