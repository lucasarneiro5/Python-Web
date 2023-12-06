import requests

url_base = 'https://jsonplaceholder.typicode.com'
url_endpoint = '/posts'

try:
    response = requests.get(url= url_base + url_endpoint)
    response.raise_for_status()

    data = response.json()
    print(data)
except requests.exceptions.HTTPError as e:
    print("An HTTP error occurred: ", e)
except requests.exceptions.RequestException as e:
    print("A request error ocurred:", e)
except Exception as e:
    print("An exception occurred: ", e)