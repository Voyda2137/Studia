from urllib.parse import urlparse

url = urlparse('https://wtie.pbs.edu.pl/pl/')
print(url.scheme)
print(url.port)
print(url.path)
