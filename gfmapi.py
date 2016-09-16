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
  print(result)

except http.client.BadStatusLine:
  traceback.print_exc()
except:
  traceback.print_exc()
