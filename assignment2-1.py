result = []

def translit(text):
    georgian = ['ა', 'ბ', 'გ', 'დ', 'ე', 'ვ', 'ზ', 'ჱ', 'თ', 'ი', 'კ', 'ლ', 'მ', 'ნ', 'ჲ', 'ო', 'პ', 'ჟ', 'რ', 'ს', 'ტ', 'ჳ', 'უ', 'ფ', 'ქ', 'ღ', 'ყ', 'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ', 'ხ', 'ჴ', 'ჯ', 'ჰ', 'ჵ']
    ipa = ['a', 'b', 'g', 'd', 'ɛ', 'v', 'z', 'ɛj', 'tʰ', 'ɪ', 'kʼ', 'l', 'm', 'n', 'j', 'ɔ', 'pʼ', 'ʒ', 'r', 's', 'tʼ', 'wi', 'u', 'pʰ', 'kʰ', 'ɣ', 'qʼ', 'ʃ', 'tʃ', 'ts', 'dz', 'tsʼ', 'tʃʼ', 'x', 'q', 'dʒ', 'h', 'hɔɛ']
    georgianIPA = dict(zip(georgian, ipa))
    for s in text:
        if s in georgian:
            text = text.replace(s, georgianIPA[s])
    return text

f = open('georgian.txt', encoding = 'utf-8')
for line in f:  # такое считывание по строчкам ведь быстрее будет для большого файла?
    result.append(translit(line))
f.close()

f = open('georgianTranslit.txt', 'w', encoding = 'utf-8')
f.write(''.join(result))
f.close()
