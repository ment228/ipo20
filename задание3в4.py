from urllib.parse import urlparse

url = urlparse('https://www.osh.by/?p=102986')
url1 = url
#<Протокол><Домен><Путь><Параметры><Запрос><Якорь>
print(f'ссылка {url1.scheme}://{url1.netloc}?{url1.path}{url1.params}{url1.query}{url1.fragment}')