import xml.etree.ElementTree as ET
import pandas as pd

data = {}
data['Question'] = []
data['Answer'] = []

i = 0
question = ''

f = open('YahooAnswers.tsv', 'w')

for event, elem in ET.iterparse("YahooAnswersDataset.xml", events=("start","end")):
    if elem.tag == "subject" and event == "end":
        question = elem.text
        question = question.replace('\t', '')

    elif elem.tag == "bestanswer" and event == "end":
        answer = elem.text
        answer = answer.replace('<br />', '')
        answer = answer.replace('\n', ' ')
        answer = answer.replace('\t', ' ')
        f.write(question + '\t' + answer + '\n')
        i += 1

    if i % 100000 == 0:
        print(i)
    if i > 3000000:
        break

f.close()
