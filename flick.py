import sys
try:
    from imgbuild import imgbuild
except ImportError:
    print('No module found.')


def main():
    if sys.argv[1]:
        im = imgbuild.imgbuilder(query=sys.argv[1])
    else:
        print('Query for images required.')
    if sys.argv[2]:
        mosaic = imgbuild.mosaicbuilder(image=sys.argv[2])
        mosaic.buildMosaic()
    else:
        print('Input picture required!') 
    
if __name__=='__main__':
    main()