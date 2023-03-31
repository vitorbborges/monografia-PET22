import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from bs4 import BeautifulSoup
import re
import time
import warnings
warnings.filterwarnings("ignore")

def isinside(string1, string2):
    words1 = re.findall(r'\w+', string1)
    words2 = re.findall(r'\w+', string2)
    found1 = all(word1 in words2 for word1 in words1)
    found2 = all(word2 in words1 for word2 in words2)
    return found1 or found2

def request(session, i):
    url = f'https://dblp.org/search/publ/api?q={pubs[i]}&format=xml'
    time.sleep(2)
    with session.get(url) as response:
        data = response.text
        return data

async def start_async_process():
    with ThreadPoolExecutor(max_workers=6) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            tasks = [loop.run_in_executor(executor, request, *(session,i)) for i in range(len(pubs))]
            codes = []
            for response in await asyncio.gather(*tasks):
                soup = BeautifulSoup(response, 'xml')
                try:
                    if soup.find('status')['code'] == '200':
                        authors = list(map(lambda x: x.text.upper(), soup.findAll('author')))
                        author_codes = list(map(lambda x: x['pid'] ,soup.findAll('author')))
                        mapa = list(map(lambda x: isinside(name, x), authors))
                        try:
                            a = authors[mapa.index(True)]
                            c = author_codes[mapa.index(True)]
                        except:
                            a = None
                            c = None
                        if c not in codes and c != None:
                            codes.append(c)
                    else:
                        time.sleep(5)
                except:
                    time.sleep(5)
            dblp_codes.append(codes)


if __name__ == "__main__":
    top = pd.read_csv('top.csv')
    top.set_index('Unnamed: 0', inplace=True)
    dblp_codes = []
    for name in top.index:
        print(name)
        pubs = eval(top.loc[name]['Papers'])
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(start_async_process())
        tries = 0
        while tries < 20:
            try:
                loop.run_until_complete(future)
                break
            except:
                tries += 1
                time.sleep(5)
                print('Error. Retrying...')
        top['DBLP'] = dblp_codes + ['']*(len(top)-len(dblp_codes))
        top.to_csv('top.csv')