/*Owner & Copyrights: Vance King Saxbe. A.*/""" Copyright (c) <2014> Author Vance King Saxbe. A, and contributors Power Dominion Enterprise, Precieux Consulting and other contributors. Modelled, Architected and designed by Vance King Saxbe. A. with the geeks from GoldSax Consulting and GoldSax Technologies email @vsaxbe@yahoo.com. Development teams from Power Dominion Enterprise, Precieux Consulting. Project sponsored by GoldSax Foundation, GoldSax Group and executed by GoldSax Manager."""from src.googlefinancequote import *
import sqlite3 as lite
import string
import gc
import time
import math
from src.dbbackup import *
import _thread
from src.goldsaxanalytics import *

def actionking(lck, tempf, stocklist, dbase, attmt,actionlist,cycle,timeatpresent,timetotake):
    if tempf == []:
        timeatpresent = time.clock()
    
    if (time.clock() - timeatpresent) > timetotake:
        return 0
    lck.acquire()
    lck.release()
    f = pullprocess(stocklist)
    sorter = []
    con = lite.connect(dbase)
    for fuck in f:
            for suck in tempf:
                    if (fuck[0] == suck[0]):
                            try:
                                Jack = float(fuck[3].replace(",",""))
                                Jill = float(suck[3].replace(",",""))
                            except ValueError:
                                break
                            if (abs(Jack-Jill)> 0.01):
                                    sorter.append(fuck[0])
                                    stmt = "INSERT INTO "+fuck[0]+"table(ONNN, ATTT, PRIC) VALUES ('"+fuck[1]+"', '"+fuck[2]+"', "+fuck[3].replace(",","")+");"
                                    cur = con.cursor()
                                    try:
                                        cur.execute(stmt)
                                        con.commit()
                                    except lite.OperationalError:
                                        
                                        time.sleep(0.05)
                                        try:
                                            cur.execute(stmt)
                                            con.commit()
                                        except lite.OperationalError:
                                            
                                            time.sleep(0.05)
                                            try:
                                                cur.execute(stmt)
                                                con.commit()
                                            except lite.OperationalError:
                                                con.commit()
                                    
    
    con.close()
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

        return null
    if tempf != [] and sorter == [] and attmt == 3:
        time.sleep(60)
        gc.collect()
        attmt = 4
        
    if tempf != [] and sorter == [] and attmt == 2:
        time.sleep(30)
        gc.collect()
        attmt = 3
        
    if tempf != [] and sorter == [] and attmt == 1:
        time.sleep(10)
        gc.collect()
        attmt = 2
        
    if tempf != [] and sorter == []:
        time.sleep(5)
        attmt = 1
        
        gc.collect()
    time.sleep(0.0001)
    gc.collect()
    cycle = cycle + 1
    
    return actionking(lck,f, stocklist,dbase, attmt,actionlist,cycle,timeatpresent,timetotake)



def pullprocess(ass):
        sds = googlefinancequote.getquote(ass)
        return sds


/*email to provide support at vancekingsaxbe@powerdominionenterprise.com, businessaffairs@powerdominionenterprise.com, For donations please write to fundraising@powerdominionenterprise.com*/