import requests
import shelve
from uuid import uuid4
import os
from PIL import Image, ImageStat
import json
from operator import sub


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
        return ImageStat.Stat(self.image).median
        # meanr, meang, meanb = 0, 0, 0
        # for x in range(self.width):
        #     for y in range(self.height):
        #         r, g, b = self.pixelgetter[x, y]
        #         meanr += r
        #         meang += g
        #         meanb += b
        # return (meanr/self.pixcount, meang/self.pixcount, meanb/self.pixcount)
imgs = ["https://www.mydick.pictures/cocks/albums/userpics/10476/1/thumb_2018-06-25_08-56-54.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_z1re1spvxd3r.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Grote_dikke_lul.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_IMG_20190129_so_fucking_BIG.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_tumblr_o24i64ODAy1uioqt4o6_1280.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_me8cock.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_cock8me.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_2019226_100397.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_images.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_IMG_20190224_035850.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_eIiPQ8mh.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_mADcrkT.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_bite2.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_bite3.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_1DB2EF3E-B461-4EB1-BCE1-6D5313E42F3E.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_BBF2E984-714A-400C-936A-24A915A82A70.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_slippery.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_lubed.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_vokx7911uvix.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_qa6s8pbkby2b.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_multixnxx-My_Forum_Favorites_II-5.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_IMG_20190115_125437366.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_IMG_20190206_094312020.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_IMG_20190215_001441.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_dVOok4n.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_My_huge_cock1028229.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_0_814b7f59-eb56-4dd5-8a30-8301157e9865.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_5F7AA3B.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_21120C3E-319F-4DC6-971F-D7BF7683A932.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_2019-02-03_12_41_29.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20190209_190227.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10339/1/thumb_20190122_031948.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_16~0.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10128/1/thumb_IMG_20180720_010619.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_image~79.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_93C7EB86-F2D2-4EE6-9517-5CFF2E56D159.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Rockhard.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Woody~0.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_ed28881e-4b38-4d66-88a1-bc25d077673f.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10100/1/thumb_IMG_4260.JPG", "https://www.mydick.pictures/cocks/albums/userpics/thumb_2193B9B2-6BB1-4991-9677-446FB52ED930.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_image~75.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_horny.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10100/1/thumb_IMG_E3636.JPG", "https://www.mydick.pictures/cocks/albums/userpics/thumb_IMG_5012.JPG", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20180828_112430.jpg",
        "https://www.mydick.pictures/cocks/albums/userpics/…1/thumb_F010E482-19FC-45DF-8CE5-4797F2F1BE42.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/…1/thumb_80A114B0-C292-4A71-8110-774E59C258A4.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/…1/thumb_3D97B8D5-03A6-49C2-BAA5-03EF4FE3AAF6.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_IMG_20190131_063127.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_CE3E3736-1486-4B09-B2BA-ED7C028E77DA.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/10218/1/thumb_manmeat.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_IMG_6048.JPG", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Z.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10241/1/thumb_53137.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_205AD037-467A-4135-93E9-4C9E077FB1AF.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_73EBB4C1-8D88-427E-817F-19F1BDCDF58E.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_39091163-3dac-4f99-9e27-23fdaca1f5ff.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_1548106926-picsay.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb__190121_162446_733.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb__190121_162432_594.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20190121_113137-01.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_0084A459-965A-4258-8D7C-3B0BF557DBB9.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_P_20181210_043956.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_P_20180811_143526.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_694E57A2-3C39-4AB6-9F18-D7FE48A2C4D2.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_C9EEB11F-0C5D-4D72-9CE9-6FA29794C269.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/10128/1/thumb_IMG_20190114_031634.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_D0479B87-A3E0-4834-B2C5-240D0702F707.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/10128/1/thumb_IMG_20180713_192827.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10150/1/thumb_2018-12-20-18-35-18-400.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_700B43BB-490D-43D1-8054-1A3F0279FD94.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_5de8b240-37b6-46a2-9381-db5bf4978ddc.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10144/1/thumb_NICE_.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10141/1/thumb_13_hot_inches.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10141/1/thumb_13_sexy_inches21.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_8D7723EC-2C3B-4E9F-A7DD-7C49563A00B7.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20190105_173842.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_CB3AF255-796B-4CAA-949F-5C995D7DAE77.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/10128/1/thumb_IMG_20190103_003723.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10128/1/thumb_IMG_20190102_175843.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_BA1CE007-E64E-4602-B244-05A3E5E35B52.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_9435F882-ABBB-4BD0-947E-59073B22E951.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Screenshot_20181124-145315_Photo_Editor.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_44.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Webp_net-compress-image.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_1546142453085-1192226033.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_a624108b-2a05-4635-bbfd-b2491141cef0.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_297b2912-d39b-47b8-9d01-1ad1e054a113.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_P_20180318_205002.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_A39BE3F2-C9D7-4151-A89E-6601B8A8BA21.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_15457828659143743759391702617106.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10100/1/thumb_20180730_075133.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_7AA47949-F966-4556-81B0-3EA35ACA4E1C.jpeg",
        "https://www.mydick.pictures/cocks/albums/userpics/thumb_IMG_20180126_013329.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_89EDE90C-C6CB-4C89-903A-4BD074AE5F5C.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_image~15.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_image~14.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_AirBrush_20180819220337.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_a6eb26048217da9501e1ce2aaff40eee.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_6EF2AECB-1F81-4F60-ABF4-F528DD2A38C2.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_73729E89-4615-4625-BF20-20BE1E4DBCA2.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_BB331D54-3F0E-4BAB-BC42-E9A773ABBF0F.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_365453CC-C30F-48B0-9495-C0CE44EBFB38.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_D8665966-D9A8-4639-987B-141DCCE12317.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_1A2EA315-F54F-437B-B67D-357396A9341E.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_313_1000.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_002_1000.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_297DC9C0-F17B-40EF-9FA8-3D7A3D4A8276.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_84E3356C-2321-4B15-BF1E-2BA8E66FA611.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_80EE1376-5802-491F-9F9A-415B1F7A24B3.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/10068/1/thumb_20181216_034714-1701x3024.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10068/1/thumb_20181017_145233.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20181216_213851.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10058/1/thumb_side.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_at88.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_received_732446300299895.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_1543540452630.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20181129_224946.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20181129_225120.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20181129_225325.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20181129_225626.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20181129_225938.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20181129_225519.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_20181129_225834.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10019/1/thumb_C4weR-s99L8.jpg", "https://www.mydick.pictures/cocks/albums/userpics/10007/1/thumb_download_28129.jpeg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_18.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_21.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_20.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_19.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_15.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_16.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_17.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_14.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_12.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_9.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_11.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_13.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_10.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_6.jpg", "https://www.mydick.pictures/cocks/albums/userpics/thumb_Big_White_Penis_7.jpg"]

class mosaicbuilder:
    def __init__(self, storage=os.path.join(os.path.dirname(__file__), 'storage'), image=None, output='mosaic_' + str(uuid4()) + '.jpg'):
        self.image = Image.open(image)
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.storage = storage
        self.pixelgetter = self.image.load()
        self.rgbs = dict()
        self.output = output
        self.openStorage()

    def openStorage(self):
        with shelve.open(self.storage) as handle:
            for image in handle:
                self.rgbs[image] = handle[image]

    def buildMosaic(self, size=64):
        result = Image.new('RGB', (self.width*size, self.height*size))
        curw = 0
        curh = 0
        for x in range(0, self.width):
            for y in range(0, self.height):
                min = (255, 255, 255)
                mmin = ''
                curPix = self.pixelgetter[x,y]
                for pix in self.rgbs:                    
                    temp = tuple(map(lambda x: abs(x), map(sub, curPix, self.rgbs[pix])))                    
                    if temp < min or not mmin:
                        min = temp
                        mmin = pix
                print('Best matching pix for {} is {}'.format(curPix, self.rgbs[pix]))
                try:
                    thumbnail = Image.open(os.path.join(os.path.dirname(__file__), 'thumbnails', mmin))
                except Exception as e:
                    thumbnail = Image.open(os.path.join(os.path.dirname(__file__), 'thumbnails', 'dickpic_1.jpg'))
                result.paste(thumbnail, box=(curw, curh))
                curh += size
                if curh == self.height*size:
                    curh = 0
                    curw += size
        result.save(self.output)
                


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
        self.getImageLinks()
        self.downloadImages()
        self.files = [file for file in self.getFiles()]
        self.buildShelve()
        self.buildThumbnails()
        self.thumbnails = [thumbnail for thumbnail in self.getThumbnails()]
        

    def getFiles(self):
        for file in filter(lambda x: x.endswith('.jpg'), os.listdir(self.storage)):
            yield file

    def getThumbnails(self):
        for file in os.listdir(self.thumbdir):
            yield file

    def buildThumbnails(self, size=(64,64)):
        if not os.path.exists(os.path.join(self.storage, self.thumbdir)):
            os.mkdir(os.path.join(self.storage, self.thumbdir))
        for num, image in enumerate(self.files):
            print('Processing %i thumbnail of %i' %(num, len(self.files)))            
            try:
                im = Image.open(os.path.join(self.storage, image))
                im = im.resize(size)
                im.save(os.path.join(self.thumbdir, image))
            except Exception as e:
                print('Skipping invalid image')

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
        for num, photo in enumerate(imgs):
            data = requests.get(photo, stream=True)
            with open(os.path.join(self.storage, f'dickpic_{num}.jpg'), 'wb') as handle:
                print('Processing %i link of %i' % (num + 1, len(self.links)))
                for buff in data.iter_content():
                    handle.write(buff)

    def buildShelve(self):
        with shelve.open(os.path.join(os.path.dirname(__file__), 'storage')) as handle:
            for num, image in enumerate(self.files):
                try:
                    print('(Shelve): Processing %i image file of %i' % (num + 1, len(self.files)))
                    im = imganalysis(os.path.join(self.storage, image))
                    pixel = im.getMeanPix()
                    handle[image] = pixel
                except Exception as e:
                    print('Skipping invalid image: ', image)
                    continue

    