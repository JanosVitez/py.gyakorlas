nev = input("Kerem, adja meg a nevet!")

ev = int(input ("Kerem,adja meg a szuletesi evet: "))

if ev> 2009: 
       print("Sajnalom, nem beazonosithato ev!")
elif ev >= 1995:
       print(f"Kedves {nev}, On Z generacios")
elif ev>=1980:
       print(f"Kedves {nev}, On Y generacios")
elif ev>=1965:
       print(f"Kedves {nev}, On X generacios")
else:
       print("Sajnalom,nem beazanosithato ev!")