import os
import json

import aiohttp
import aiofiles
import asyncio
import logging

from typing import Optional


logger = logging.getLogger(__name__)

FLICKR_SEARCH_BY_TERM_URL = 'https://api.flickr.com/services/rest/?' \
                            'method=flickr.photos.search&text={}&api_key={}&format=json'
FLICKR_RECENT_PHOTOS_URL = 'https://api.flickr.com/services/rest/?' \
                           'method=flickr.photos.getRecent&api_key={}&format=json'


class FlickrImageDownloader:
    def __init__(self, storage_dir: str, token: str):
        self.storage_dir = storage_dir
        self.token = token

    async def download_images(self,
                              search_term: Optional[str] = None,
                              images_limit: int = 100):
        url = FLICKR_RECENT_PHOTOS_URL.format(self.token)
        if search_term:
            logger.info('Downloading images by search term: %s.', search_term)
            url = FLICKR_SEARCH_BY_TERM_URL.format(search_term, self.token)
        else:
            logger.info('Downloading images by recent Flickr API.')
        if not os.path.exists(self.storage_dir):
            logger.info('Storage directory not found, creating new one with path %s', self.storage_dir)
            os.makedirs(self.storage_dir, mode=0o777)
        image_links = await self._get_image_links(url)
        await asyncio.gather(*[self._download_image(image_info) for image_info in image_links],
                             return_exceptions=True)

    async def _download_image(self, image_info):
        logger.info('Downloading image %s.', image_info['name'])
        target_file_name = os.path.join(self.storage_dir, f"{image_info['name']}.jpg")
        async with aiohttp.request('GET', image_info['url']) as response:
            async with aiofiles.open(target_file_name, 'wb') as file_handler:
                async for data in response.content.iter_chunked(n=1048):
                    await file_handler.write(data)
        logger.info('Done downloading image %s.', image_info['name'])

    async def _get_image_links(self, url):
        image_links = []
        response = await self._request(url)
        for photo in response['photos']['photo']:
            image_links.append(self._parse_image_link(photo))
        logger.info('Done getting photos info from Flickr. Gathered info on %s images.',
                    len(image_links))
        return image_links

    @staticmethod
    def _parse_image_link(photo_response):
        return {
            'url': f'https://farm{photo_response["farm"]}.staticflickr.com/{photo_response["server"]}'
                   f'/{photo_response["id"]}_{photo_response["secret"]}_n.jpg',
            'name': photo_response['secret']
        }

    @staticmethod
    async def _request(url):
        async with aiohttp.request('GET', url) as response:
            response_body = await response.text()
            response_body = response_body.lstrip('jsonFlickrApi(').rstrip(')')
            return json.loads(response_body)

