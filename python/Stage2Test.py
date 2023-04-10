import os
import spacy
import re as regex
from saxonc import PySaxonProcessor  # Use saxonc instead of saxonche for Python 3.9+

nlp = spacy.load('en_core_web_lg')

# Define the path to your XML files
CollPath = '../source-xml'

# Define the named entity types you are interested in
interesting_entities = {'PERSON', 'ORG', 'GPE'}

# Define the output file name
output_file = 'named_entities.tsv'

# Open the output file in write mode
with open(output_file, 'w', encoding='utf-8') as f_out:
    # Write the header row to the output file
    f_out.write('File\tEntity\tEntity Type\n')

    # Loop through all the XML files in the collection directory
    for filename in os.listdir(CollPath):
        if filename.endswith('.xml'):
            filepath = os.path.join(CollPath, filename)

            # Read and process each XML file
            with PySaxonProcessor(license=False) as proc:
                xml = open(filepath, encoding='utf-8').read()
                xp = proc.new_xpath_processor()
                node = proc.parse_xml(xml_text=xml)
                xp.set_context(xdm_item=node)

                # Extract the text from the <p> elements
                xpath = xp.evaluate('//book//p ! normalize-space() => string-join()')
                string = str(xpath)
                cleaned_up = regex.sub("(\.)([A-Z']])", "\1 \2", string)
                tokens = nlp(cleaned_up)

                # Collect named entities
                for ent in tokens.ents:
                    if ent.label_ in interesting_entities:
                        f_out.write(f'{filename}\t{ent.text}\t{ent.label_}\n')

print(f'Saved named entities to {output_file}.')
