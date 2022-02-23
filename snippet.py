import ezscrape
import requests
url = requests.get("https://code1tech.repl.co")
Scraper = ezscrape.Scraper(url.content, 'html.parser', warningsmode=True)
oofclass = Scraper.sfaewac('oof')
print(str(oofclass)) 
