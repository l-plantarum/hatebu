# はてなブックマークのコメントを標準出力に出力する
import urllib.request
import urllib.parse
import sys
import json

url = sys.argv[1]
encurl = urllib.parse.quote(url, safe='')
resp = urllib.request.urlopen('http://b.hatena.ne.jp/entry/jsonlite/' + encurl)
b64str = resp.read()
bkmstr = b64str.decode()
bkminfo = json.loads(bkmstr)
if bkminfo is None:
    sys.exit()
for it in bkminfo['bookmarks'] :
    if it['comment'] != '':
         print(it['comment'])
