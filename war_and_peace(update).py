from collections import Counter
import re

ignoreList = ['the', 'a','an', 'in', 'at', 'near', 'over', 'under', 'between', 'to', 'from', 'off', 'by'
                  'since', 'for', 'оn', 'in', 'before', 'after', 'and', 'but', 'or', 'if', 'that', 'when', 'of',
                  'so', 'as', 'until', 'because', 'while', 'with']
n = "|".join(ignoreList)
c = re.compile(r'\b(?!(?:'+n+'))\w{3,}')

def text_war_and_peace_without_ignoreList():

    with open('Tolstoy_War_and_Peace.txt', 'r') as file:
        text = file.read()
        words = re.findall(c, text)
        top_10 = Counter(words).most_common(10)
        print(top_10)
text_war_and_peace_without_ignoreList()
