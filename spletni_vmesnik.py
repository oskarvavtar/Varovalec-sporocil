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

# CEZARJEVA ŠIFRA
@bottle.get("/cezarjeva-sifra")
def cezarjeva_sifra():
    return bottle.template("cezarjeva_sifra.html")


# SUBSTITUCIJA+
@bottle.get("/substitucija-plus")
def substitucija_plus():
    return bottle.template("substitucija_plus.html")

#
# @bottle.post("/substitucija-plus-zakodirano")
#def zakodiraj_sub_plus():
    
    
bottle.run(reloader=True, debug=True)