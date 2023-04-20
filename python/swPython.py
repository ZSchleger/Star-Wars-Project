
# pip install saxonche
import os
import spacy
import re as regex
from saxonche import PySaxonProcessor


# nlp = spacy.cli.download("en_core_web_lg")
nlp = spacy.load('en_core_web_lg')

CollPath = '../xml'


def readTextFiles(filepath):
    with PySaxonProcessor(license=False) as proc:
        xml = open(filepath, encoding='utf-8').read()
        xp = proc.new_xpath_processor()
        node = proc.parse_xml(xml_text=xml)
        xp.set_context(xdm_item=node)

        xpath = xp.evaluate('(//script//sp/text(), //script//sd, //script//crawl) ! normalize-space() => string-join()')
        string = str(xpath)

        cleanedUp = regex.sub("(\.)([A-Z']])", "\1 \2", string)
        doc = nlp(cleanedUp)
        person_dict = entitycollector(doc)

        return person_dict



def entitycollector(doc):
    with open('output.txt', 'w') as f:
        person_dict = {}
        for entity in doc.ents:
            if entity.label_ == 'PERSON':
                person_name = entity.text
                if person_name not in person_dict:
                    person_dict[person_name] = {'count': 1, 'verbs': []}
                else:
                    person_dict[person_name]['count'] += 1

                # use Spacy to analyze text in sp element and pick out verbs
                sp_text = entity.root.head.text
                sp_doc = nlp(sp_text)
                for token in sp_doc:
                    if token.pos_ == 'VERB':
                        person_dict[person_name]['verbs'].append(token.lemma_)

        print(f"{person_dict=}")
        return person_dict



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
