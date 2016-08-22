from caesar import encrypt
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        answer = encrypt("Hello, Zach!", 2)
        self.response.write(answer)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
