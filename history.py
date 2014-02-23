""" Copyright (c) <2014> Author Vance King Saxbe. A, and contributors Power Dominion Enterprise, Precieux Consulting and other contributors. Modelled, Architected and designed by Vance King Saxbe. A. with the geeks from GoldSax Consulting and GoldSax Technologies email @vsaxbe@yahoo.com. Development teams from Power Dominion Enterprise, Precieux Consulting. Project sponsored by GoldSax Foundation, GoldSax Group and executed by GoldSax Manager."""import urllib3
import sqlite3
import string
from time import localtime, strftime
import time
import re

def cleanhtml(raw_html):

  cleanr =re.compile('<.*?>')
  
  cleantext = re.sub(cleanr,'', raw_html)
  cleantext = cleantext.split('\n')
  content=[]
  for text in cleantext:
      if text!='':
        content.append(re.sub(',', '', text))
  return content

   
def gethistory(stock):
  kuka = sqlite3.connect("history/INDIAHISTORY.db")
  cura = kuka.cursor()
  stmt = "CREATE TABLE IF NOT EXISTS "+stock+"table(DATE TEXT, OPEN REAL, HIGH REAL, LOW REAL, CLOSE REAL, VOLUME REAL)"
  cura.execute(stmt)
  kuka.commit()
  signal ="TRUE"
  if stock == "BANKBEES" or stock == "BANSWRAS" or stock == "BANKINDIA":
    signal="FALSE"

  count = 0
  finaldict = {}
  
  print("Started on ",stock)
  while signal!="FALSE":
          url = "https://www.google.com/finance/historical?q=NSE:"+stock+"&histperiod=weekly&startdate=27/01/1994&enddate=27/01/2014&output&start="+str(count)+"&num=30"
          count+=30
          http = urllib3.PoolManager()
          try:
              r = http.request('GET', url)
              r.release_conn()
          except urllib3.exceptions.MaxRetryError:
              signal ="FALSE"
    
          f = r.data.decode("latin-1")
          try:
            firstsplit = f.split('<table class="gf-table historical_price">')
            secondsplit = firstsplit[1].split('</table>')
            
            thirdsplit = secondsplit[0].split('<tr>')
            
            for split in thirdsplit:
                items = cleanhtml(split)
                tstamp = re.sub(',', '', items[0])
                tstamp = tstamp.split(' ')
                if len(tstamp)>1:
                  numero=[0,1,2,3,4,5,6,7,8,9]
                  dte=tstamp[1]
                  for num in numero:
                      if tstamp[1]==num:
                        dte='0'+str(num)
                  stampt=tstamp[0]+"-"+dte+"-"+tstamp[2]
                
                
                  import datetime
                  d = datetime.datetime.strptime(stampt, '%b-%d-%Y')
                  stamp = d.strftime('%d-%m-%Y')
                  items.pop(0)
                  import collections
                  for x in range(5):
                    if items[x] == "-" or items[x] == "'-'":
                      items.pop(x)
                      items.insert(x,items[3])
                      
                  try:
                    stmtw = "INSERT INTO "+stock+"table(DATE, OPEN, HIGH, LOW, CLOSE, VOLUME) VALUES ('"+stamp+"', '"+items[0]+"', "+items[1]+", "+items[2]+", "+items[3]+", "+items[4]+");"
                    cura.execute(stmtw)
                    kuka.commit()
                  except sqlite3.OperationalError:
                      print("ERROR ",stmtw)
          except IndexError:
                  signal ="FALSE"
          
          time.sleep(10)
          print("contitnuing on ", stock, " for count ", count)
  kuka.close()
  print("Finished on ",stock)
  return 0

kuk = sqlite3.connect("data/INDIA.db")
cur = kuk.cursor()
stmt = "SELECT PRIC FROM ANZAXtable WHERE ONNN = '2014-01-24';"
stmta = "SELECT name FROM sqlite_master WHERE type = 'table'"
stmta = "SELECT name FROM sqlite_master WHERE type = 'table'"
cur.execute(stmta)
row = cur.fetchall()
kuk.commit()
kuk.close()

fur=[]
for ro in row:
  symb = ro[0]
  symbo = symb[0:-5]
  gethistory(symbo)
