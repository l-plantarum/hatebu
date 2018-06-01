  1 # はてなブックマークのコメントを標準出力に出力する
  2 import urllib.request
  3 import urllib.parse
  4 import sys
  5 import json
  6
  7 url = sys.argv[1]
  8 encurl = urllib.parse.quote(url, safe='')
  9 resp = urllib.request.urlopen('http://b.hatena.ne.jp/entry/jsonlite/' + encu    rl)
 10 b64str = resp.read()
 11 bkmstr = b64str.decode()
 12 bkminfo = json.loads(bkmstr)
 13 for it in bkminfo['bookmarks'] :
 14     if it['comment'] != '':
 15         print(it['comment'])
