import logging
import spacy
logging.basicConfig(filename='ErrorLog.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)


def writeResultFile(countNouns,countVerbs):
    try:
        file1 = open("Result.txt","w")
        file1.write("Nouns Count - "+str(countNouns) +"\n")
        file1.write("Verbs Count - "+str(countVerbs) +"\n")
        print(countNouns,countVerbs)
        file1.close() 
    except Exception as Argument:
        logger.error(Argument)
try:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(open("TextFile.txt").read())
    nouns=[token.text for token in doc if token.is_stop != True and token.is_punct !=True and token.pos_=='NOUN']
    verbs=[token.text for token in doc if token.is_stop != True and token.is_punct !=True and token.pos_=='VERB']
    writeResultFile(len(nouns),len(verbs))
except Exception as Argument:
        logger.error(Argument)




