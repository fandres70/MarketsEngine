""" Copyright (c) <2014> Author Vance King Saxbe. A, and contributors Power Dominion Enterprise, Precieux Consulting and other contributors. Modelled, Architected and designed by Vance King Saxbe. A. with the geeks from GoldSax Consulting and GoldSax Technologies email @vsaxbe@yahoo.com. Development teams from Power Dominion Enterprise, Precieux Consulting. Project sponsored by GoldSax Foundation, GoldSax Group and executed by GoldSax Manager."""import urllib3
import string
from time import localtime, strftime

class googlefinancequote:
    
    def getquote(url):
            http = urllib3.PoolManager()
            try:
                r = http.request('GET', url)
                r.release_conn()
            except urllib3.exceptions.MaxRetryError:
                time.sleep(120)
                http = urllib3.PoolManager()
                try:
                    r = http.request('GET', url)
                    r.release_conn()
                except urllib3.exceptions.MaxRetryError:
                    print("Once retried Yahoo and failed")
                    return contents
            except ConnectionResetError:
                time.sleep(120)
                http = urllib3.PoolManager()
                try:
                    r = http.request('GET', url)
                    r.release_conn()
                except ConnectionResetError:
                    print("Once retried Yahoo and failed")
                    return contents
            f = r.data.decode("latin-1")
            a = f.split('"t" : "')
            tstamp = strftime("%H:%M:%S", localtime())
            count = 0
            contents = []
            for ass in a:
                if count > 0:
                    v = ass.split('"\n,"e" : "')
                    h = ass.split(',"l" : "')
                    j = h[1].split('"\n,"l_')
                    #filename = strftime("%Y-%m-%d", localtime())+"_"+v[0]+".csv"
                    #text_file = open(filename, "a")
                    #text_file.write(tstamp+", "+j[0]+"\n")
                    #text_file.close()
                    contents.append([v[0],strftime("%Y-%m-%d"),tstamp,j[0]])
                count = count+1
            return contents

