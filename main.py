
import logging
import urllib2
import webapp2

class UrlHandler(webapp2.RequestHandler):

    def get(self):
        # [START urllib-get]
        url = 'http://www.google.com/humans.txt' # change this to the URL you want to call
        try:
            result = urllib2.urlopen(url)
            self.response.write(result.read())
        except urllib2.URLError:
            logging.exception('Caught exception fetching url')
        # [END urllib-get]

app = webapp2.WSGIApplication([
    ('/tasks/humans', UrlHandler)
], debug=True)
