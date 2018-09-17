from sys import argv

import bottle
from bottle import *

@route("/")

def index():
    return """
    <h1>Verkefni 3</h1>
    <p><a href="/a">Liður A</></p>
    <p><a href="/b">Liður B</a></p>
    """
@route("/a")

def index():
    return template("tempA.tpl")

@route("/sida/<kt>")

def index(kt):
    return template("temp_kt.tpl",kt=kt)

frettir = [["Irma veldur usla á Flórída", "Það er bara ... vesen á Irmu í Flórída.  Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...", "dsg@frettir.is"],
           ["Veiðin er dræm þetta haustið", "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", "est@frettir.is"],
           ["Ólafía stendur sig vel", "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", "htg@frettir.is"],
           ["Ísland dottið úr leik", "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", "dsg@frettir.is"]]


@route("/b")

def index():
    return template("tempB.tpl",frettir=frettir)

@route("/frett/<id:int>")

def index(id):
    return template("frett.tpl",frett=frettir[id],nr=id)


@error(404)
def villa(error):
    return "<h2>Error 404: Not Found</h2>"

@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root="./static")

bottle.run(host="0.0.0.0", port=argv[1])
