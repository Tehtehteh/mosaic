import asyncio

from logger import setup_logging
from args import parse_args
from mosaic_workers.image_downloader import FlickrImageDownloader


async def main():
    setup_logging()
    config = parse_args()
    image_downloader = FlickrImageDownloader(storage_dir=config.storage_dir,
                                             token=config.token)
    await image_downloader.download_images(search_term=config.search_term)


if __name__ == '__main__':
    asyncio.run(main())
