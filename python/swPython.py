
# pip install saxonche
import os
import spacy
import re as regex
from saxonche import PySaxonProcessor


# nlp = spacy.cli.download("en_core_web_lg")
nlp = spacy.load('en_core_web_lg')

CollPath = './xml'


def readTextFiles(filepath):
    with PySaxonProcessor(license=False) as proc:
        xml = open(filepath, encoding='utf-8').read()
        xp = proc.new_xpath_processor()
        node = proc.parse_xml(xml_text=xml)
        xp.set_context(xdm_item=node)

        xpath = xp.evaluate('//script//sp ! normalize-space() => string-join()')
        string = str(xpath)

        cleanedUp = regex.sub("(\.)([A-Z']])", "\1 \2", string)
        tokens = nlp(cleanedUp)
        listEntities = entitycollector(tokens)

        return(listEntities)



def entitycollector(tokens):
    with open('output.txt', 'w') as f:
        entities = {}
        for entity in tokens.ents:
            if entity.label_ == 'PERSON':
                entityText = entity.text
                if entityText not in entities:
                    entities[entityText] = 1
                else:
                    entities[entityText] += 1

        for entity, count in entities.items():
            entityInfo = [entity, count]
            stringify = str(entityInfo)
            print(stringify)
            f.write(stringify)
            f.write('\n')
        print(f"{entities=}")
        return entities




def assembleAllNames(CollPath):
    AllNames = []
    for file in os.listdir(CollPath):
        if file.endswith(".xml"):
            filepath = f"{CollPath}/{file}"
            print(filepath)
            print(readTextFiles(filepath))
            eachFileList = readTextFiles(filepath)
            print(eachFileList)
            AllNames.append(eachFileList)
    print(AllNames)
    print(len(AllNames))

    flatList = [element for innerList in AllNames for element in innerList]

    distinctNames = set(flatList)

    print(f"{distinctNames=}")
    print('AllNames Count: ' + str(len(AllNames)) + ' : ' + 'Distinct Names Count: ' + str(len(distinctNames)) + ' : ' + 'flatList Count ' + str(len(flatList)))
    with open('distNames.txt', 'w') as f:
        f.write(str(distinctNames))
    return distinctNames

assembleAllNames(CollPath)
