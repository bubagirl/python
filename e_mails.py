import re
n= input("Открыть текстовый файл : ")
list = []
m = re.compile(r'\w+@\w+.\w+')
with open(n, 'r') as file:
    for line in file:
        list.extend(m.findall(line))
print(list)
