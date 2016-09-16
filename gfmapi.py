#!/usr/bin/env python3

import traceback
import json
import urllib.request
import http.client
import sys

try:
  content = sys.stdin.read()
  data = {
    'text': content,
    'mode': 'gfm'
  }
  headers = {
    'Content-Type':
    'application/json'
  }
  bytes = json.dumps(data).encode('utf-8')
  url = 'https://api.github.com/markdown'

  request = urllib.request.Request(url, data=bytes, headers=headers)
  result = urllib.request.urlopen(request).read().decode('utf-8')

  html_header = (
    '<?xml version="1.0" encoding="UTF-8" ?> '
    '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" '
    '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
    '<html xmlns="http://www.w3.org/1999/xhtml"> '
    '<head> '
    '<title>Markdown Rendering from GitHub</title> '
    '<meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>  '
    '<link rel="stylesheet" type="text/css" '
    'href="https://cdn.rawgit.com/sindresorhus/github-markdown-css/'
    'gh-pages/github-markdown.css"> '
    '<style>.markdown-body {box-sizing: border-box; min-width: 200px; '
    'max-width: 980px; margin: 0 auto; padding: 45px; }</style>'
    '</head>'
    '<body class="markdown-body">')

  html_footer = (
    '</body>'
    '</html>')

  print(html_header)
  print(result)
  print(html_footer)

except http.client.BadStatusLine:
  traceback.print_exc()
except:
  traceback.print_exc()
