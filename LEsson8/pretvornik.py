zelipretvorbu="da"
km=0
milje=0

while zelipretvorbu=="da":

    km=int(raw_input("unesi broj za prevorbu u milje:"))
    milje=km/1.609
    print "to je" + str(milje) + "milja"
    zelipretvorbu=str(raw_input("zelis li pretvorbu da ili ne:"))
