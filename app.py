from email import message
from unicodedata import name
from xml.etree.ElementTree import tostring ;
import createFile ;
from flask import Flask, jsonify, render_template ;


app = Flask(__name__,template_folder="/serving_static")

@app.route("/")
def hello_world():
    return "hello"

@app.route("/get/<wikiurl>/<USER_KEY>")
def getpairs(wikiurl,USER_KEY):
    #return createFile.run(wikiurl)
    data = createFile.run(wikiurl,USER_KEY)
    return jsonify({'data':data})

if __name__ == "__main__":
    app.run(debug=True) 



#response = createFile.run("Yuzuki_Akiyama")

#print(response)


