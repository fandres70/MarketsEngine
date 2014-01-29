import numpy as np
import sqlite3 as lite
import re
from numpy import warnings
import scipy
import _thread
from time import localtime, strftime
class goldsaxanalytics:
  def fetch(symbol, databse, loc):
    con = lite.connect(databse)
    today = strftime("%Y-%m-%d", localtime())
    stmta = "SELECT PRIC FROM "+symbol+"table WHERE ONNN = '"+today+"';"
    cur = con.cursor()
    loc.acquire()
    loc.release()
    act = 0
    if 1:
      try:                               
        cur.execute(stmta)
        con.commit()
        
        row = cur.fetchall()
        con.close()
      except lite.OperationalError:
           return 0
       
      
    
    
    
    furr=[]
    
    for roo in row: 
        try:
                furr.append(float(re.sub('[^0-9.]+', '', str(roo))))
        except ValueError:
                act = 1
    
    if act != 1 and furr != []:
      tikk = givecoeffs(furr)
      if tikk[0] ==1:
        
    
        connn = lite.connect('data/ANALYTICS.db')
        stmta = "INSERT INTO ANALYTIC(ASSET, PRIC, COMMENTS) VALUES ('"+symbol+"', '"+str(furr[-1])+"', '"+str(tikk[1])+"');"
        currr = connn.cursor()
        
        currr.execute(stmta)
      
        connn.commit()
        connn.close()
        
        #print( "ASSET ", symbol, " from ", databse, " is ", furr[-1],tikk[1],"/n")
    
    return 0
            
    act = 0

import numpy as np
from numpy import polyfit
from numpy import poly1d

previous =0
def givecoeffs(fur):
    x = np.array(np.linspace(1,len(fur),len(fur)))
    y = np.array(fur)
    
    z = np.polyfit(x,y,15)
    warnings.simplefilter('ignore', np.RankWarning)
    s = z.sum()
    t=[]
    for zz in z:
        t.append(zz)
    de = poly1d(np.array(t))
    det = np.polyder(de)
    dett = np.polyder(det)
  
    if (dett(len(fur)) < 0 and det(len(fur)) > 0) or (dett(len(fur)) > 0 and det(len(fur)) < 0) or det(len(fur)) ==0 or dett(len(fur))==0 :
      return 1, poly1d(np.array(t))
    else:
      return 0,0
  
