import requests
import time

api = "key"

test_req = requests.get(f"https://api.vk.com/method/fave.get?", params={
    'count': 1,
    'access_token': api,
    'v': 5.131
}).json()
all_pages = test_req['response']['count']

while all_pages != 1:
    all_pages -= 1
    post = requests.get(f"https://api.vk.com/method/fave.get?", params={
        'count': 1,
        'access_token': api,
        'v': 5.131
    }).json()
    author = post['response']['items'][0]['post']['owner_id']
    id_post = post['response']['items'][0]['post']['id']
    ls = requests.get("https://api.vk.com/method/fave.removePost?", params={
        'owner_id': int(author),
        'id': int(id_post),
        'access_token': api,
        'v': 5.131
    })
    time.sleep(1)

print("Deleted!")
