consonants = []
vowels = []
amharicA = {}
result = ''

def translit(text, amharicA):
    translitR = ''
    punc = {'።':'.', '፣':',', '፤':';', '፥':':'} # кажется, в той новостной статье, что в файле amharicText.txt используются
# другие символы для знаков преписания, но я не нашла подходящую таблицу соответствий и взяла, видимо, не очень новую из википедии
    for symbol in text:
        if symbol in amharicA.keys():
            translitR += amharicA[symbol]
        elif symbol in punc.keys():
            translitR += punc[symbol]
        else:
            translitR += symbol
    return translitR

with open('amharic.tsv', encoding = 'utf-8') as f:
    c = 0
    for line in f:
        line = line.strip("\n")
        line = line.split("\t")
        v = 0
        for symbol in line:
            symbol = symbol.strip(" ")
            if c == 0 and v != 0:
                vowels.append(symbol)
            if c != 0 and v == 0:
                consonants.append(symbol)
            if c != 0 and v != 0:
                amharicA[symbol] = consonants[c-1] + vowels[v-1]
            v += 1
        c += 1

with open('amharicText.txt', encoding = 'utf-8') as f:
    for line in f:
        result += translit(line, amharicA)
		
with open('amharicTranslit.txt', 'w', encoding = 'utf-8') as f:
    f.write(result)



    
