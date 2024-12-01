import requests

# setting up API key and endpoint
API_KEY = 'your_api_key_here'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

# define parameters
params = {
    'country': 'us',
    'catergory': 'technology',
    'apikey': API_KEY
}

# api requests
response = requests.get(BASE_URL, params=params)

# check if request succesful
if response.status_code == 200:
    data = response.json()
    for article in data['articles']:
        print(f'Title: {article['title']}')
        print(f'Date: {article['publishedAt']}')
        print(f'Descript: {article['description']} \n')
else:
    print(f'Error: {response.status_code} - {response.json()}')