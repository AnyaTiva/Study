import re

with open('dilPage.txt', encoding = 'utf-8') as f:
    page = f.read()
    result = re.search('<h3.*?>\d*(.*?)</h3>.*Forms:\s*(.*?)</p>', page)
    if result != None:
        lemma = result.group(1)
        tokens = result.group(2)
    tokens = tokens.split(' ')
    Result = {}
    for token in tokens:
        token = token.strip(",")
        Result[token] = lemma

with open('dilOutput.txt', 'w', encoding = 'utf-8') as f:
     for item in Result:
        f.write(item + ' --' + Result[item] + '\n')
