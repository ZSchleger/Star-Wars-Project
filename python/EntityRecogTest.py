import spacy
from collections import Counter
import os

nlp = spacy.load("en_core_web_lg")

workingDir = os.getcwd()
print("Current working directory: " + workingDir)

# Define the path to the folder containing the Star Wars XML text files
CollPath = os.path.join(workingDir, '')

def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        stringFile = str(readFile)
        tokens = nlp(stringFile)
        listEntities = entitycollector(tokens)
        print(listEntities)

def entitycollector(tokens):
    entities = []
    for entity in tokens.ents:
        print(entity.text, entity.label_, spacy.explain(entity.label_))
        entities.append(entity.text)
    return entities

# Loop through the files in the Star Wars XML folder
for file in os.listdir(CollPath):
    if file.endswith(".xml"):
        filepath = os.path.join(CollPath, file)
        print(filepath)
        readTextFiles(filepath)
