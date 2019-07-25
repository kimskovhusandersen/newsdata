#!/usr/bin/env python3
#
# A web report based on a newsdata log.

from flask import Flask

from newsdb import get_top_articles, get_top_authors, get_errors

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>News article log</title>
    <style>
      h1, h2, form { text-align: center; font-family: Garamond;}
      h3 { color: #333; font-size: 16px;
            display: inline-block;
            text-transform: uppercase; }
      h3.title {font-style: italic;}
      span.stat { color: #333; font-size: 16px;
                  display: inline-block;
                  text-transform: lowercase;
                  font-style: normal;}
      hr { color: #666; margin-left: 45%%; margin-right: 45%%; }
      div.log { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
    </style>
  </head>
  <body>
    <h1>Newsdate Log</h1>
    <div class=log>
    <h2>Top 3 articles by views</h2> <hr>
%s
    </div>
    <div class=log>
    <h2>Top 3 authors by article views</h2> <hr>
%s
    </div>
    <div class=log>
    <h2>Dates on which requests errors were above 1%%</h2> <hr>
%s
    </div>
  </body>
</html>
'''

# HTML template for an individual comment
TOP_ARTICLES = '''\
    <h3 class=title>"%s" <span class=stat> &mdash; %s views</span></h3><br>
'''
TOP_AUTHORS = '''\
    <h3 class=author>%s <span class=stat> &mdash; %s views</span></h3><br>
'''
ERRORS = '''\
   <h3>%s <span class=stat> &mdash; %s%% (status code: 404)</span></h3><br>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''
    top_articles = "".join(
        TOP_ARTICLES % (title, num) for title, num in get_top_articles())
    top_authors = "".join(
        TOP_AUTHORS % (author, num) for author, num in get_top_authors())
    errors = "".join(
        ERRORS % (date, error_ratio) for date, error_ratio in get_errors())
    html = HTML_WRAP % (top_articles, top_authors, errors)
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
