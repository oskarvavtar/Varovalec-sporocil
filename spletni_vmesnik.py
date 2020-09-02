import bottle
import model

app = bottle.Bottle()

@bottle.get("/")
def main_page():
    return bottle.template("osnovna.html")

# ROT13
@bottle.get("/rot13")
def rot13():
    return bottle.template("rot13.html")

@bottle.get("/rot13/kodirano")
def rot13_kodiraj():
    #tekst = 
    
    model.besedilo = model.Besedilo(tekst)
    output = model.besedilo.rot13()

    return bottle.template("izpis.html", output = output) 

# CEZARJEVA ŠIFRA
@bottle.get("/cezarjeva-sifra")
def cezarjeva_sifra():
    return bottle.template("cezarjeva_sifra.html")

@bottle.get("/cezarjeva-sifra/zakodirano")
def cezarjeva_sifra_zakodiraj():
    #tekst =
    #kljuc =

    
    model.besedilo = model.Besedilo(tekst)
    model.besedilo.nastavi_geslo(kljuc)
    output = model.besedilo.cezarjeva_sifra(True)

    return bottle.template("izpis.html", output = output)

@bottle.get("/cezarjeva-sifra/dekodirano")
def cezarjeva_sifra_dekodiraj():
    #tekst =
    #kljuc =

    
    model.besedilo = model.Besedilo(tekst)
    model.besedilo.nastavi_geslo(kljuc)
    output = model.besedilo.cezarjeva_sifra(False)

    return bottle.template("izpis.html", output = output)

# SUBSTITUCIJA+
@bottle.get("/substitucija-plus")
def substitucija_plus():
    return bottle.template("substitucija_plus.html")

@bottle.get("/substitucija-plus/zakodirano")
def substitucija_plus_zakodiraj():
    #tekst = str(bottle.request.query["besedilo"])
    #kljuc = str(bottle.request.query["kljuc"])
    tekst = "challe salle"
    kljuc = "12345"

    model.besedilo = model.Besedilo(tekst)
    model.besedilo.nastavi_geslo(kljuc)
    output = model.besedilo.substitucija_po_stevkah(True)

    return bottle.template("izpis.html", output = output)

@bottle.get("/substitucija-plus/dekodirano")
def substitucija_plus_dekodiraj():
    #tekst =
    #kljuc =

    model.besedilo = model.Besedilo(tekst)
    model.besedilo,nastavi_geslo(kljuc)
    output = model.besedilo.substitucija_po_stevkah(False)

    return bottle.template("izpis.html", output = output)
    
# POLIGRAFSKA SUBSTITUCIJA
@bottle.get("/poligrafska-substitucija")
def poligrafska_substitucija():
    return bottle.template("poligrafska_substitucija.html")

@bottle.get("/poligrafska-substitucija/kodirano")
def poligrafska_substitucija_kodiraj():
    #tekst =
    #kljuc =

    model.besedilo = model.Besedilo(tekst)
    model.besedilo.nastavi_geslo(kljuc)
    output = model.besedilo.poligrafska_substitucija()

    return bottle.template("izpis.html", output = output)

bottle.run(reloader=True, debug=True)