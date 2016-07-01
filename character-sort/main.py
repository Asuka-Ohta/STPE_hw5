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
import webapp2

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/result" method="POST">
      word1: <input name="word1" type="text" />
      <br>
      word2: <input name="word2" type="text" />
      <button type="submit">sort!</button>
    </form>
  </body>
</html>
"""

RESULT_PAGE_HTML = """\
<html>
  <body>
    <form action="/result" method="POST">
      result: <input name="result" type="text" />
      <br>
      <br>
      word1: <input name="word1" type="text" />
      <br>
      word2: <input name="word2" type="text" />
      <button type="submit">again sort!</button>
    </form>
  </body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)


class ResultHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(RESULT_PAGE_HTML)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/result', ResultHandler),
], debug=True)
