import requests

url = 'https://us-central1-civil-partition-333301.cloudfunctions.net/cloud-function-proyect'
myobj = {'keyword': 'cars'}

x = requests.post(url, data = myobj)

print(x.text)