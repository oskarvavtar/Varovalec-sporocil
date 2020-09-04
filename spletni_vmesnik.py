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

@bottle.post("/rot13")
def rot13_kodiraj():
    tekst = bottle.request.forms.getunicode("tekst")
    
    model.besedilo = model.Besedilo(tekst)
    
    try: 
        output = model.besedilo.rot13()
    except Exception as err:
        output = err.args[0]

    return bottle.template("izpis.html", output = output) 

# CEZARJEVA ŠIFRA
@bottle.get("/cezarjeva-sifra")
def cezarjeva_sifra():
    return bottle.template("cezarjeva_sifra.html")

@bottle.post("/cezarjeva-sifra")
def cezarjeva_sifra_kodiraj():
    kljuc = bottle.request.forms.getunicode("kljuc")
    tekst = bottle.request.forms.getunicode("tekst")
    kodiranje = bool(int(bottle.request.forms.get("kodiranje")))

    model.besedilo = model.Besedilo(tekst)
    model.besedilo.nastavi_geslo(kljuc)
    
    try:
        output = model.besedilo.cezarjeva_sifra(kodiranje)
    except Exception as err:
        output = err.args[0]

    return bottle.template("izpis.html", output = output)

# SUBSTITUCIJA+
@bottle.get("/substitucija-plus")
def substitucija_plus():
    return bottle.template("substitucija_plus.html")

@bottle.post("/substitucija-plus")
def substitucija_plus_kodiraj():
    kljuc = bottle.request.forms.getunicode("kljuc")
    tekst = bottle.request.forms.getunicode("tekst")
    kodiranje = bool(int(bottle.request.forms.get("kodiranje")))

    model.besedilo = model.Besedilo(tekst)
    model.besedilo.nastavi_geslo(kljuc)

    try: 
        output = model.besedilo.substitucija_po_stevkah(kodiranje)
    except Exception as err:
        output = err.args[0]

    return bottle.template("izpis.html", output = output)
    
# POLIGRAFSKA SUBSTITUCIJA
@bottle.get("/poligrafska-substitucija")
def poligrafska_substitucija():
    return bottle.template("poligrafska_substitucija.html")

@bottle.post("/poligrafska-substitucija")
def poligrafska_substitucija_kodiraj():
    kljuc = bottle.request.forms.getunicode("kljuc")
    tekst = bottle.request.forms.getunicode("tekst")
    
    model.besedilo = model.Besedilo(tekst)
    model.besedilo.nastavi_geslo(kljuc)
    
    try: 
        output = model.besedilo.poligrafska_substitucija()
    except Exception as err:
        output = err.args[0]

    return bottle.template("izpis.html", output = output)

bottle.run(reloader=True, debug=True)