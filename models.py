from google.appengine.ext import ndb


class Photo(ndb.Model):
    photoid = ndb.StringProperty()
    tags    = ndb.StringProperty()
    url     = ndb.StringProperty()
    blobKey = ndb.BlobKeyProperty()

