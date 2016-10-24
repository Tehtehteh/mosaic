try:
    from imgbuild import imgbuild
except ImportError:
    print('No module found.')


def main():
    im = imgbuild.imgbuilder()
    #im.getImageLinks()
    #im.downloadImages()
    #print(im.files)
    #im.buildShelve()
    #im.buildThumbnails()
    #print(im.thumbnails)
    mosaic = imgbuild.mosaicbuilder()
    mosaic.buildMosaic()
    
main()