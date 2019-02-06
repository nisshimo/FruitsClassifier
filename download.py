from flickrapi import FlickrAPI
from urllib.request import urlretrieve
# from pprint import pprint
import os, time, sys

# APIキーの情報

key = "b3a30c7b678f6386627cfffdfd0ba77f"
secret = "a0ec13bd768e47d0"
wait_time = 0.01

# 保存フォルダの設定
fruitname = sys.argv[1]
savedir = "./" + fruitname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text=fruitname,
    per_page=400,
    media='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q, licance'
)

photos = result['photos']
# 返り値を表示する
# pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath):
        continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
