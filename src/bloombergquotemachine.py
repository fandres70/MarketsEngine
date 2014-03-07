/*Owner & Copyrights: Vance King Saxbe. A.*/""" Copyright (c) <2014> Author Vance King Saxbe. A, and contributors Power Dominion Enterprise, Precieux Consulting and other contributors. Modelled, Architected and designed by Vance King Saxbe. A. with the geeks from GoldSax Consulting and GoldSax Technologies email @vsaxbe@yahoo.com. Development teams from Power Dominion Enterprise, Precieux Consulting. Project sponsored by GoldSax Foundation, GoldSax Group and executed by GoldSax Manager."""from src.bloombergquote import *
import sqlite3 as lite
import string
import gc
import time
import math

def actionking(tempf, stocklist, dbase):
    
            
    f = pullprocess(stocklist)
    
    con = lite.connect(dbase)
    Jack = float(f[3].replace(",",""))
    Jill = float(tempf[3].replace(",",""))
                            
    if (abs(Jack-Jill)> 0.01):
                                    
                                    stmt = "INSERT INTO "+f[0]+"table(ONNN, ATTT, PRIC) VALUES ('"+f[1]+"', '"+f[2]+"', "+f[3].replace(",","")+");"
                                    cur = con.cursor()
                                    try:
                                        cur.execute(stmt)
                                    except lite.OperationalError:
                                        print("database locked for ", f[0])
                                        time.sleep(0.25)
                                        try:
                                            cur.execute(stmt)
                                            print("tried once & executed for ", f[0])
                                        except lite.OperationalError:
                                            print("database still locked for", f[0])
                                            time.sleep(0.25)
                                            try:
                                                cur.execute(stmt)
                                                print("tried twice & executed for ", f[0])
                                            except lite.OperationalError:
                                                print("database still still locked.... fuckkk offff...", f[0]," is being pissing into...")
    con.commit()
    con.close()                                
    time.sleep(5)
    gc.collect()
    return actionking(f, stocklist,dbase)

def pullprocess(ass):
        sds = bloombergquote.getquote(ass)
        return sds

def chunky(exchangeandstocks):
    return [exchangeandstocks[i:i+54] for i in range(0, len(exchangeandstocks), 54)]


/*email to provide support at vancekingsaxbe@powerdominionenterprise.com, businessaffairs@powerdominionenterprise.com, For donations please write to fundraising@powerdominionenterprise.com*/