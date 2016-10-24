import requests
import shelve
import os
from PIL import Image
import json

#todo [{'url':url, 'name': name}] for file list when creating initial image storage --- Done
#todo build shelve based of PIL 

class imgbuilder:
    def __init__(self, query=None):
        self.secret = '21ffc097f4a4d72815fff49ea0d74b1b'
        self.query = query
        if not query:
            self.url = 'https://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key={}&format=json'.format(self.secret)
        else:
            self.url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&text={}&api_key={}&format=json'.format(self.query, self.secret)
        self.storage = os.path.join(os.path.dirname(__file__), 'storage')

    def getImageLinks(self):
        self.links = []
        self.respond = requests.get(self.url)
        if not self.respond.ok:
            raise RuntimeError
        else:
            jsonresp = json.loads(self.respond.text.split('jsonFlickrApi(')[1][:-1])
        for photo in jsonresp['photos']['photo']:            
            self.links.append({ 'url' : 'https://farm{0}.staticflickr.com/{1}/{2}_{3}_n.jpg'.format(photo['farm'], photo['server'], photo['id'], photo['secret']),
                                'name':  photo['secret']})

    def downloadImages(self):
        if not os.path.exists(self.storage):
            os.mkdir(self.storage)
        for num, photo in enumerate(self.links):
            data = requests.get(photo['url'], stream=True)
            with open(os.path.join(self.storage, '{}.jpg'.format(photo['name'])), 'wb') as handle:
                print('Processing %i of %i' % (num + 1, len(self.links)))
                for buff in data.iter_content():
                    handle.write(buff)

    def buildShelve(self):
        for image in self.links:
             im = Image.open(os.path.join(self.storage, image['name']))