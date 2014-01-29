import urllib3
import string
from time import localtime, strftime

class bloombergquote:
    
    def getquote(symbol):
            url = "http://www.bloomberg.com/quote/"+symbol
            http = urllib3.PoolManager()
            r = http.request('GET', url)
            r.release_conn()
            f = r.data.decode("UTF-8")
            a = f.split('span class="ticker_data">')
            b = []
            tstamp = strftime("%H:%M:%S", localtime())
            contents = []
            try:
                b = a[1].split('</span>')
                contents.extend(symbol.replace(':',''))
                contents.extend(strftime("%Y-%m-%d"))
                contents.extend(tstamp)
                contents.extend(b[0])
            except IndexError:
                print("Index error")
            
            
            return contents

