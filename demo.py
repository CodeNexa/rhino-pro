import requests

# Sample usage of the secure proxy
proxy = 'http://127.0.0.1:8080'
response = requests.get('http://example.com', proxies={'http': proxy, 'https': proxy})
print(response.text)