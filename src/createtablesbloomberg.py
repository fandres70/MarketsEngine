from src.bloombergquote import *
import sqlite3 as lite
import string
import time

print ("Market Place Starts.......")

def pullprocess(ass):
        sds = bloombergquote.getquote(ass)
        return sds
def createtables(arguments):
        f = pullprocess(arguments[0])
        print ("Counter One Started.........")
        if f != []:
                con = lite.connect(arguments[1]+".db")
                fuck = f
                stmt = "CREATE TABLE IF NOT EXISTS "+fuck[0]+"table(ONNN TEXT, ATTT TEXT, PRIC REAL)"
                cur = con.cursor()
                cur.execute(stmt)
            
                con.commit()
                time.sleep(2)
                con.close()

    
    
