import os ;
import requests ;
import openai ;
import numpy ;
from bs4 import BeautifulSoup ;
from nltk import PunktSentenceTokenizer ;



#function generates array of paragraphs
def textArray(URL) :
    pst = PunktSentenceTokenizer()
    html_text = requests.get(URL).text 
    soup = BeautifulSoup(html_text, 'html.parser')
    textExport = []
    text = []
    for para in soup.find_all("p"):
        sentenceBlock = pst.tokenize(para.get_text())
        text.append(sentenceBlock)
    
    for block in text :
        for crumb in block:
            textExport.append(crumb)

    return textExport

    


    





if __name__ == "__main__":
    print(textArray("https://en.wikipedia.org/wiki/Mao_Chaofeng"))