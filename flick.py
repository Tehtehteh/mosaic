from imgbuild import imgbuild


def main():
    im = imgbuild.imgbuilder()
    im.getImageLinks()
    im.downloadImages()

main()