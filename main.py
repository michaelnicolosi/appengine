
# importing the requests library 
import requests 
import webapp2
import urllib2

class HourCronPage(webapp2.RequestHandler):
    def get(self):
        request = urllib2.Request('<GCF URL>', headers={"cronrequest" : "true"})
        contents = urllib2.urlopen(request).read()

app = webapp2.WSGIApplication([
    ('/minute', HourCronPage),
    ], debug=True)

endpoint = 'https://google-analytics.com/collect?v=1&t=event&tid=UA-121324737-1&cid=43789789.23578678&ec=appengine&ea=mm-protocol&el=some-test'
  
# sending post request and saving response as response object 
r = requests.post(url = endpoint) 
