try:
    from imgbuild import imgbuild
except ImportError:
    print('No module found.')


def main():
    im = imgbuild.imgbuilder()
    im.getImageLinks()
    im.downloadImages()

main()