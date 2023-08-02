import pymongo

# ----------------------------------------------------------------------------------------------
# 1. Erstellen Sie die Klasse Bücher. Die aufgenommen Objekte sollen folgende „Attribute“
#    aufweisen:name, vorname, jahr, titel, verlag, P NEU, P_GEBR
# ----------------------------------------------------------------------------------------------


class Books:
    def __init__(self, name, vorname, jahr, titel, verlag, neupreis, gebrauchtpreis):
        self.name = name
        self.vorname = vorname
        self.jahr = jahr
        self.titel = titel
        self.verlag = verlag
        self.neupreis = neupreis
        self.gebrauchtpreis = gebrauchtpreis
        self.differenz = neupreis - gebrauchtpreis

# ----------------------------------------------------------------------------------------------
# 2. Erzeugen Sie eine Ausgabe – Methode, die das Buch wie folgt ausgibt.
#    Hetland, M. L. (2014). Python Algorithms: mastering basic algorithms in
#    the Python Language. Apress
# ----------------------------------------------------------------------------------------------

    def ausgabe(self):
        print(f"{self.name}, {self.vorname}, ({self.jahr}). {self.titel}. {self.verlag}.")

    def database_entry(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["literature"]
        dokumente = mydb["documents"]
        neue_literatur = {"nachame": self.name, "vorname": self.vorname, "jahr": self.jahr,
                          "titel": self.titel, "verlag": self.verlag,
                          "neupreis": self.neupreis, "gebrauchtpreis": self.gebrauchtpreis}
        dokumente.insert_one(neue_literatur)


buch_1 = Books("Hetland", "M. L.", 2014, "Python Algorithms: mastering basic \
algorithms in the Python Language", "Apress", 120, 20)

buch_1.ausgabe()
buch_1.database_entry()

# ----------------------------------------------------------------------------------------------
# 3. Die Bücher sollen mit ihren spezifischen Angaben über Tastatureingaben
#    eingelesen werden. (als Objekt erzeugt werden)
#
#    Nicht in Aufgabenstellung enthalten: Eingabe Möglichkeit von mehreren
#    Büchern, die direkt in die Datenbank gespeichert werden mit der
#    Methode der Books Class. Hier wird für jede Eingabe automatisch das neue
#    Objekt Buch in einer Liste gespeichert und danach zur Kontrolle ausgegeben.
#
# 4. Erzeugen Sie folgendes Buch als Objekt:
#    Summerfield, M. (2010). Programming in Python 3: a complete introduction
#    to the Python language. Addison-Wesley Professional.
# ----------------------------------------------------------------------------------------------
buch_liste = []

while True:
    eingabe_autor = input("Bitte geben Sie den Nachnamen ein (oder 'q' zum Beenden): ")
    if eingabe_autor.lower() == 'q':
        break

    elif eingabe_autor.strip():
        eingabe_vorname = input("Bitte geben Sie den Vornamen ein: ")
        eingabe_jahr = input("Bitte geben Sie das Jahr ein: ")
        eingabe_titel = input("Bitte geben Sie den Titel ein: ")
        eingabe_verlag = input("Bitte geben Sie den Verlag ein: ")
        eingabe_neupreis = input("Bitte geben Sie den Neupreis ein: ")
        eingabe_gebrauchtpreis = input("Bitte geben Sie den Gebrauchtpreis ein: ")
        eingabe_neupreis = float(eingabe_neupreis)
        eingabe_gebrauchtpreis = float(eingabe_gebrauchtpreis)

        buch = Books(eingabe_autor, eingabe_vorname, eingabe_jahr, eingabe_titel,
                    eingabe_verlag, eingabe_neupreis, eingabe_gebrauchtpreis)

        buch_liste.append(buch)
        buch.ausgabe()
        buch.database_entry()

for buch in buch_liste:
    buch.ausgabe()

# ----------------------------------------------------------------------------------------------
# 6. Erzeuge folgendes Objekt in der „Klasse Article“ (Die Klasse soll von
#    der „Klasse Books“ erben)
#
#    Madnani, N. (2007). Getting started on natural language processing with
#    Python. The ACM Magazine for Students, 13(4), 5-5.
#    Class Article ist hier, sollte aber eigentlich bei der anderen Class 
#    Books sein, wegen gutem Style
# ----------------------------------------------------------------------------------------------


class Article(Books):

    def __init__(self, name, vorname, jahr, titel, verlag, neupreis, gebrauchtpreis, journal, band, seitenzahl):
        Books.__init__(self, name, vorname, jahr, titel, verlag, neupreis, gebrauchtpreis)
        self.journal = journal
        self.band = band
        self.seitenzahl = seitenzahl

    def ausgabe(self):
        print(f"{self.name}, {self.vorname}, ({self.jahr}). {self.titel}. \
{self.verlag}, {self.journal}, {self.band}, {self.seitenzahl}.")

    def database_entry(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["literature"]
        dokumente = mydb["documents"]
        neue_literatur = {"nachame": self.name, "vorname": self.vorname, "jahr": self.jahr,
                          "titel": self.titel, "verlag": self.verlag,
                          "neupreis": self.neupreis, "gebrauchtpreis": self.gebrauchtpreis,
                          "journal": self.journal, "band": self.band, "seitenzahl": self.seitenzahl}
        dokumente.insert_one(neue_literatur)


article = Article("Madnani", "N.", 2007, "Getting started on natural language processing with Python",
                  "XRDS:Crossroads", 10, 0, "The ACM Magazine for Students", "13(4)", "5-5")

article.ausgabe()

article.database_entry()

# ----------------------------------------------------------------------------------------------
# 7. Das erzeugte Objekt soll in MongoDB – Datenbank „literature“ in einer
#    Collection „documents“ abgespeichert werden.
#
#    Ohne die Methode Database_entry (zu Fuß)
# ----------------------------------------------------------------------------------------------

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# mydb = myclient["literature"]

# dokumente = mydb["documents"]

# neue_literatur = {"nachame": article.name, "vorname": article.vorname, "jahr": article.jahr,
#                   "titel": article.titel, "verlag": article.verlag,
#                   "neupreis": article.neupreis, "gebrauchtpreis": article.gebrauchtpreis,
#                   "journal": article.journal, "band": article.band, "Seitenzahl": article.seitenzahl}

# dokumente.insert_one(neue_literatur)
