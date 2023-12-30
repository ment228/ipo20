from urllib.parse import urlparse
url = urlparse('://www.osh.by/?p=102986')
print(url)
#добавление протокола к URL-адресу
url._replace(scheme='https')
print(url)