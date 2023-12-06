import requests

url_base = 'https://httpbin.org'

# Realizando method GET
url_endpoint = '/get'


response_get = requests.get(url=url_base + url_endpoint)
print('Headers: ', response_get.headers)
print('\nTexto: ', response_get.text)

if response_get.status_code == 200:
    print('\nFormato json: ', response_get.json())
    print('\nDicionario com chave dos headers: ', response_get.json()['headers'])
else:
    print(response_get.content)


# Realizando method POST
url_endpoint = '/post'

response_post = requests.post(url=url_base + url_endpoint)

response_post_dict = response_post.json()
print('\nResposta methodo POST: ', response_post_dict)