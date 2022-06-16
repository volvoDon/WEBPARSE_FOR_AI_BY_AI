import os ;
import csv ;
import requests ;
import openai ;
import numpy ;
from bs4 import BeautifulSoup ;
from nltk import PunktSentenceTokenizer ;
from dotenv import load_dotenv ;

#See README.txt for full overview

#function generates array of sentences from html from http request
#INPUT = URL in form of a string as argument 
#OUTPUT = Array of sentences

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

#Function Creates A JSON file of prompt/completion pairs using GPT 3 
#Input = Array of sentences
#output = {"prompt1":"sentence1","prompt2:sentence2"...} prompt generated by GPT
class theMind :
    def toCSV(ARRAY,API_KEY):
        QA_pairs = [["prompt","completion"]]
        openai.api_key = API_KEY
        for block in ARRAY :
            textPrompt = "\What question would illicit this completion:\n"+"\ncompletion: "+block+"\n"+"\nprompt:"
            
            completion = openai.Completion.create(engine="text-curie-001", prompt=textPrompt,temperature=.05)
            
            textcompletion = completion.choices[0].text

            QA_pairs.append([textcompletion,block]) 

        with open('output.csv', 'w') as f:
            # create the csv writer
            writer = csv.writer(f)

            for block in QA_pairs : # write a row to the csv file
                writer.writerow(block)
        
        
#function exports jsonl for testing and training 
#the next version will create a tuned model directly
#I don't want my card linked to this unsteady monster right away

    

if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    text = textArray("https://en.wikipedia.org/wiki/Zoltán_Opata")
    theMind.toCSV(text,API_KEY)
    print("done")