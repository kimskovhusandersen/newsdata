#!/usr/bin/env python3
#
# An internal newsdata reporting tool

from flask import Flask

from newsdb import get_top_articles, get_top_authors, get_errors

app = Flask(__name__)

# HTML template for the newsdata log page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Newsdate Log</title>
  </head>
  <body>
    <h1>Newsdate Log</h1>
    <h2>Top 3 articles by views:</h2>
%s
    <h2>Top 3 authors by article views:</h2>
%s
    <h2>Dates on which requests errors were above 1%%:</h2>
%s
  </body>
</html>
'''

# HTML template for an top three articles and authors
TOP_THREE = '''\
- %s &mdash; %s views<br>
'''
# HTML template for an request errors above 1%
ERRORS = '''\
- %s <span class=stat> &mdash; %s%% (status code: 404)<br>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''
    top_articles = "".join(
        TOP_THREE % (title, num) for title, num in get_top_articles())
    top_authors = "".join(
        TOP_THREE % (author, num) for author, num in get_top_authors())
    errors = "".join(
        ERRORS % (date, error_ratio) for date, error_ratio in get_errors())
    html = HTML_WRAP % (top_articles, top_authors, errors)
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
