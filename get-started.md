# Getting started with EzScrape

Here is a little code snippet that you can modify in your own ways:  
```python
import ezscrape
import requests
url = requests.get("https://code1tech.repl.co")
Scraper = ezscrape.Scraper(url.content, 'html.parser', warningsmode=True)
oofclass = Scraper.sfaewac('oof')
print(str(oofclass))
```
------
Here is a more in depth version.  
```python
import ezscrape
import requests

# The URL to scrape.
url = requests.get("https://code1tech.repl.co")

# Initialize the Scraper class.
#  URL HTML (x.content recommened) | The parser to use (bs4) | Warnings mode turns off exceptions. Default is "False".
Scraper = ezscrape.Scraper(url.content, 'html.parser', warningsmode=True)
# "sfaewac" is the short form for SearchForAllElementsWithAClass()
oofclass = Scraper.sfaewac('oof')
#                class name ^^^

# Sets off a warning because the "hello" ID is not on the website.
test = Scraper.sfaewai("hello")

oofclass = str(oofclass)
print(oofclass)
```
----------
# These files will be available to download.
