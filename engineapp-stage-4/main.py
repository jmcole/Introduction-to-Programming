#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import urllib
from google.appengine.ext import ndb
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

template_dir = os.path.join(os.path.dirname(__file__),'templates')
# based on google guestbook example
DEFAULT_GUESTBOOK_NAME = 'default_guestbook'

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    return ndb.Key('Guestbook', guestbook_name)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        "Render jija2 templates"
        t = JINJA_ENVIRONMENT.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        "Write the jinja template to the website"
        self.write(self.render_str(template, **kw))

class Greeting(ndb.Model):
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(Handler):

    def get(self):
        self.render("templates/index.html")

class NotePage(Handler):

    def get(self):
        self.render("templates/Lesson_1.html")

class NotePage2(Handler):

    def get(self):
        self.render("templates/Lesson_2.html")

class NotePage3(Handler):

    def get(self):
        self.render("templates/Lesson_3.html")

class NotePage4(Handler):

    def get(self):
        self.render("templates/Lesson_4.html")

class NotePage5(Handler):

    def get(self):
        self.render("templates/Lesson_5.html")

class Respage(Handler):
    def get(self):
        self.render("templates/add_res.html")
class Cycpage(Handler):
    def get(self):
        self.render("templates/cyclemap.html")

class Guestbook(webapp2.RequestHandler):

    def post(self):
        guestbook_name = self.request.get('guestbook_name',DEFAULT_GUESTBOOK_NAME)
        greeting = Greeting(parent=guestbook_key(guestbook_name))
        greeting.content = self.request.get('content')
        if greeting.content == "":
            self.response.out.write('Error! No comment entered. Please click back on your browser')
        else:
            greeting.put()
            query_params = {'guestbook_name': guestbook_name}
            #self.redirect('/?' + urllib.urlencode(query_params))
            self.redirect('comments')


class ErrorHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("error")


class CommentPage(webapp2.RequestHandler):
    def get(self):
        guestbook_name = self.request.get('guestbook_name',DEFAULT_GUESTBOOK_NAME)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch()
        template_values = {
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
        }
        template = JINJA_ENVIRONMENT.get_template('templates/comments.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainPage),('/add_res', Respage),('/Lesson_1',NotePage),('/Lesson_2',NotePage2),
    ('/Lesson_3',NotePage3),('/Lesson_4',NotePage4),('/Lesson_5',NotePage5),
    ('/sign', Guestbook),('/error', ErrorHandler),('/comments',CommentPage),('/cyclemap',Cycpage),
], debug=True)
