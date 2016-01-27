import os, urllib.request 
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = 'http://m-v-news.ru/novosti'
urls = [url]
urlsVisited = [url]
userAgent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
headers = {'User-Agent':userAgent}

while len(urls) > 0:
    try:
        req = urllib.request.Request(urls[0], headers)
        connection = urllib.request.urlopen(req)
        if connection.getcode() == 200:
            htmltext = connection.read().decode("utf-8")
            file = urls[0].split('/')[-1] + '.html'
            filename = os.path.join('C:/Corpus/', file)
            with open(filename, 'w', encoding = 'utf-8') as f:
                f.write(htmltext)
                
            htmlNew = BeautifulSoup(htmltext, "html.parser")
            urls.pop(0)
            print(len(urls))

            links = htmlNew.findAll('a', href = True)
#           или links = re.findall('href=[\'"]?([^\'" >]+)', str(htmltext)) ...
            for tag in links:
                tag['href'] = urljoin(url, tag['href'])
                if url in tag['href'] and tag['href'] not in urlsVisited:
                    urls.append(tag['href'])
                    urlsVisited.append(tag['href'])
    except:
        print(urls[0])


