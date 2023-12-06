import requests

url_base = 'https://jsonplaceholder.typicode.com'

# Method GET
url_endpoint = '/posts/'

response = requests.get(url=url_base+url_endpoint)
if response.status_code == 200:
    pass
    #print('Conteudo: ', response.json())
else:
    print('Erro: ', response.content)

# Method POST
body = {
    "userId": 1,
    "body": "Teste",
    "title": "Software Engineerig fo Data Engineering"
}

# De acordo com a documentacao, necessario header
header = {'Content-type': 'application/json; charset=UTF-8',}

response_post = requests.get(url=url_base+url_endpoint, 
                                data=body,
                                headers=header)
if response_post.status_code in range(200, 300, 1):
    pass
    #print('\nConteudo POST: ', response_post.json())
else:
    print('\nErro POST: ', response_post.content)


# Adicionando parametros apos a ?
post_id = '1'
resource_post = 'comments'
path_param = '/'.join([post_id, resource_post])

#Testando com os parametros montados:
response = requests.get(url=url_base + url_endpoint + path_param)
print('\nRespostas da API, apos param: ', response.json())