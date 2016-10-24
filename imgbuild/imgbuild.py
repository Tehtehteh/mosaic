import requests
import shelve
import os
from glob import glob
from PIL import Image
import json
from operator import sub

#todo [{'url':url, 'name': name}] for file list when creating initial image storage --- Done
#todo build shelve based of PIL 

class imganalysis:
    def __init__(self, path=None):
        if not path or not os.path.exists(path):
            print(path, '--- not exists?')
            raise RuntimeError
        else:
            self.image = Image.open(path)
            self.width = self.image.size[0]
            self.height = self.image.size[1]
            self.pixelgetter = self.image.load()
            self.pixcount = self.width * self.height

    def getMeanPix(self):
        meanr, meang, meanb = 0, 0, 0        
        for x in range(self.width):
            for y in range(self.height):
                r, g, b = self.pixelgetter[x, y]
                meanr += r
                meang += g
                meanb += b
        return (meanr/self.pixcount, meang/self.pixcount, meanb/self.pixcount)

class mosaicbuilder:
    def __init__(self, storage=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'storage'), image='1.jpg'):
        self.image = imganalysis(image)
        self.storage = storage
        self.rgbs = None
        self.openStorage()

    def openStorage(self):
        with shelve.open(self.storage) as handle:
            for image in handle:
                self.rgbs[image] = handle[image]


    def buildMosaic(self):
        #assert image, storage != (None, None), 'No image/storage supplied'
        result = Image.new('RGB', (self.image.width, self.image.height)).load()
        for num, x in enumerate(range(self.image.width)):
            print('Processing %i of width %i' % (num, self.image.width))
            for numy, y in enumerate(range(self.image.height)):
                print('Processing %i of height %i' % (numy, self.image.height))
                curPix = self.image.pixelgetter[x, y]
                min = (255, 255, 255)
                for pix in self.storage:
                    temp = tuple(map(lambda x: abs(x), map(sub, self.storage[pix])))
                    if temp < min:
                        min = temp
                result[x,y] = min
        result.save('result.jpg')
                


class imgbuilder:
    def __init__(self, query=None):
        self.secret = '21ffc097f4a4d72815fff49ea0d74b1b'
        self.query = query
        if not query:
            self.url = 'https://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key={}&format=json'.format(self.secret)
        else:
            self.url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&text={}&api_key={}&format=json'.format(self.query, self.secret)
        self.storage = os.path.join(os.path.dirname(__file__), 'storage')
        self.thumbdir = os.path.join(os.path.dirname(__file__), 'thumbnails')
        self.thumbnails = [thumbnail for thumbnail in self.getThumbnails()]
        self.files = [file for file in self.getFiles()]

    def getFiles(self):
        for file in filter(lambda x: x.endswith('.jpg'), os.listdir(self.storage)):
            yield file

    def getThumbnails(self):
        for file in os.listdir(self.thumbdir):
            yield file

    def buildThumbnails(self, size=(64,16)):
        if not os.path.exists(os.path.join(self.storage, self.thumbdir)):
            os.mkdir(os.path.join(self.storage, self.thumbdir))
        for num, image in enumerate(self.files):
            print('Processing %i thumbnail of %i' %(num, len(self.files)))            
            im = Image.open(os.path.join(self.storage, image))
            im.thumbnail(size)
            im.save(os.path.join(self.thumbdir, image))

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
        else:
            pass
        for num, photo in enumerate(self.links):
            data = requests.get(photo['url'], stream=True)
            with open(os.path.join(self.storage, '{}.jpg'.format(photo['name'])), 'wb') as handle:
                print('Processing %i of %i' % (num + 1, len(self.links)))
                for buff in data.iter_content():
                    handle.write(buff)

    def buildShelve(self):
        print('Building shelve.')
        for num, image in enumerate(self.files):
            print('Processing %i of %i' % (num + 1, len(self.files)))
            im = imganalysis(os.path.join(self.storage, image))
            pixel = im.getMeanPix()
            with shelve.open('storage') as handle:
                handle[image] = pixel

    