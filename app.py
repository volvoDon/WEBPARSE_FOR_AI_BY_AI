from unicodedata import name
from xml.etree.ElementTree import tostring ;
import createFile ;
from flask import Flask ;
from flask import url_for ;

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World but Different!</p>"

@app.route("/getpairs/<wikiurl>")
def getpairs(wikiurl):
    #return createFile.run(wikiurl)
    return f'Pair {createFile.run(wikiurl)}'



#response = createFile.run("https://en.wikipedia.org/wiki/Yuzuki_Akiyama")

#print(response)


