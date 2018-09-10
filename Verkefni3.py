#from sys import argv

from bottle import *

@route("/page1")

def index():
    return template("index1.tpl")

@route("/page2")

def index():
    return template("index2.tpl")

@route("/page3")

def index():
    return template("index3.tpl",nafn="Óskar")

@route("/page4")

def index():
    my_dict={"number":"89","street":"Cool street","city":"Cool City"}
    return template("index4.tpl", my_dict)

@route("/page5")

def index():
    info={"title":"Beatles","names":["Ringo","Paul","John","George"]}
    return template("index5.tpl", info)

@error(404)
def villa(error):
    return "<h2>Error: 404 Not Found</h2>"

@route("/Images/<skra>")
def static_skra(skra):
    return static_file(skra, root="Images")
run(host="Localhost", port=8080, reloader=True, debug=True)

#bottle.run(host="0.0.0.0", port=argv[1])
