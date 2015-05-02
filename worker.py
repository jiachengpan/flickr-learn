import flickr
import settings

import logging

flickr.API_KEY      = settings.key
flickr.API_SECRET   = settings.secret

flickr.debug        = True


class FlickrWorker(object):
    @staticmethod
    def searchPhotos(text):
        return flickr.photos_search(text=text)
