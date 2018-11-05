from collections import Counter
import re
def read_text():
    Ignore = ['the', 'a','an', 'in', 'at', 'near', 'over', 'under', 'between', 'to', 'from', 'off', 'by'
                  'since', 'for', 'оn', 'in', 'before', 'after', 'and', 'but', 'or', 'if', 'that', 'when', 'of',
                  'so', 'as', 'until', 'because', 'while', 'with']
    n = "|".join(Ignore)
    with open('Tolstoy_War_and_Peace.txt', 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b(?!(?:'+n+'))\w{2,}', text)
        top_10 = Counter(words).most_common(10)
        print(top_10)
read_text()
