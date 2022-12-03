import urllib.request
import re
from bs4 import BeautifulSoup

wikipedia = urllib.request.urlopen(
    'https://pl.wikipedia.org/wiki/Python').read()
# regex, który sprawdza czy linki kończą się 'wikipedia.org.Python'
regex = re.compile(r"\bwikipedia[.]\borg[/]\bwiki[/]\bPython$")
# odczytanie wszystkich elementów HTML
soup = BeautifulSoup(wikipedia, "html.parser")
# znalezienie wszystkich linków
for link in soup.findAll('a', attrs={'href': regex}):
    print(link.get('href'))
