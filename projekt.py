#vajadzīgās bibliotēkas
from requests_html import HTMLSession

sesija = HTMLSession()
#vieta = 'riga'
try:
    vieta = input("Kādas lokācijas laikapstākļus jūs vēlētos uzzināt? ") #lietotājs ievada lokāciju
    url = f'https://www.google.com/search?q=google+weather+{vieta}' #google weather urls+ievadītā lokācija
    req = sesija.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}) #veicam piepraījumu ar my user agent palīdzību
    
    # izviltie dati
    laiks = (req.html.find('div.VQF4g', first=True).find('div.wob_dts', first=True).text)
    temp = (req.html.find('span#wob_tm', first=True).text)
    celsijas = (req.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text)
    apraksts = (req.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text)
except:
    print("Kļūda, mēģinat vēlreiz!")
    
# print(apraksts)

#printējam ārā tekstu kopā ar izvadītajiem datiem
print("Šodien, "+laiks.replace(",","") +', '+vieta.capitalize()+" , temperatūra ārā ir "+ temp + celsijas+" un ārā ir " + apraksts.lower())
