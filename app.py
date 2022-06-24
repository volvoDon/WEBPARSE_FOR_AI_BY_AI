from unicodedata import name
from xml.etree.ElementTree import tostring ;
import createFile ;
from flask import Flask, jsonify ;


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World but Different!</p>"

@app.route("/getpairs/<wikiurl>/<USER_KEY>")
def getpairs(wikiurl,USER_KEY):
    #return createFile.run(wikiurl)
    data = createFile.run(wikiurl,USER_KEY)
    return jsonify({'data':data}) 



#response = createFile.run("Yuzuki_Akiyama")

#print(response)


