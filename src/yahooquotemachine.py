from src.yahoofinancequote import *
import sqlite3 as lite
import string
import gc
import time
import math
import re
from src.goldsaxanalytics import *
import _thread
def actionking(lck, tempf, stocklist, dbase, attmt, actionlist,cycle,timeatpresent,timetotake):
    if tempf == []:
        timeatpresent = time.clock()
    
    if (time.clock() - timeatpresent) > timetotake:
        return 0
    
    f = pullprocess(stocklist)
    sorter = []
    
    
    for fuck in f:
            for suck in tempf:
                    if (fuck[0] == suck[0]):
                            Jack = float(fuck[3].replace(",",""))
                            Jill = float(suck[3].replace(",",""))
                            
                            if (abs(Jack-Jill)> 0.01):
                                    name = fuck[0]
                                    for act in actionlist:
                                        actor = act.split("=")        
                                        if name==actor[0]:
                                            name = actor[1]
                                    name = re.sub('[^a-zA-Z]+', '', name)
                                    sorter.append(name)
                                    stmt = "INSERT INTO "+name+"table(ONNN, ATTT, PRIC) VALUES ('"+fuck[1]+"', '"+fuck[2]+"', "+fuck[3].replace(",","")+");"
                                    con = lite.connect(dbase)
                                    cur = con.cursor()
                                    try:
                                        
                                        cur.execute(stmt)
                                        con.commit()
                                        con.close()
                                    except lite.OperationalError:
                                       
                                        time.sleep(0.05)
                                        try:
                                            
                                            cur.execute(stmt)
                                            con.commit()
                                            con.close()
                                            
                                        except lite.OperationalError:
                                            
                                            time.sleep(0.05)
                                            try:
                                                
                                                cur.execute(stmt)
                                                con.commit()
                                                con.close()
                                                
                                            except lite.OperationalError:
                                                con.close()
                                                time.sleep(0.005)
                                        
                                    
    
    if sorter != []:
        attmt = 0
        """
      a_lock = _thread.allocate_lock()
      with a_lock:
          for item in sorter:
               _thread.start_new_thread(goldsaxanalytics.fetch,(item,dbase,a_lock))
            """
          
    if tempf != [] and sorter == [] and attmt == 4:
        gc.collect()
        print("No data..for ",dbase)
        lck.exit()
        return null
    if tempf != [] and sorter == [] and attmt == 3:
        time.sleep(120)
        gc.collect()
        attmt = 4
    if tempf != [] and sorter == [] and attmt == 2:
        time.sleep(45)
        gc.collect()
        attmt = 3
    if tempf != [] and sorter == [] and attmt == 1:
        time.sleep(20)
        gc.collect()
        attmt = 2
    if tempf != [] and sorter == []:
        time.sleep(5)
        attmt = 1
        gc.collect()
    time.sleep(1)
    gc.collect()
    return actionking(lck, f, stocklist,dbase, attmt,actionlist,cycle,timeatpresent,timetotake)

def pullprocess(ass):
        sds = yahoofinancequote.getquote(ass)
        return sds
