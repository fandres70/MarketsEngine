/*Owner & Copyrights: Vance King Saxbe. A.*/""" Copyright (c) <2014> Author Vance King Saxbe. A, and contributors Power Dominion Enterprise, Precieux Consulting and other contributors. Modelled, Architected and designed by Vance King Saxbe. A. with the geeks from GoldSax Consulting and GoldSax Technologies email @vsaxbe@yahoo.com. Development teams from Power Dominion Enterprise, Precieux Consulting. Project sponsored by GoldSax Foundation, GoldSax Group and executed by GoldSax Manager."""#!/usr/bin/env python3
import _thread
import os
import sys
import time
import gc
from src import googlequotemachine
from src import yahooquotemachine
from src import bloombergquotemachine
from src import createtablesgooglefinance
from src import createtablesyahoofinance
from src import createtablesbloomberg
from time import localtime, strftime
start1 = []
sys.setrecursionlimit(1000000)
database = "data/"
markettime = {}
with open("conf/MarketTimings.conf") as fillees:
        mlist = fillees.read().splitlines()
fillees.close()
for line in mlist:
        items = line.split(", ")
        key, values = items[0], items[1]
        markettime[key] = values

with open('conf/symbolname.conf') as fille:
   synamelist = fille.read().splitlines()
fille.close()
timetorun = 1800
cycle = 1
while("TRUE"):
        with open('conf/urls.conf') as openedfile:
            fileaslist = openedfile.read().splitlines()
        openedfile.close()
        a_lock = _thread.allocate_lock()
        thr = []
        with a_lock:
                print("locks placed and Market engine is running for the...", cycle)
                for lines in fileaslist:
                        lisj = lines.split('", "')
                        mtime = markettime[lisj[2].replace('"','')]
                        mktime = mtime.split("-")
                        if mktime[1] < mktime[0]:
                                righto = mktime[1].split(":")
                                close = str(str(int(righto[0])+24)+":"+righto[1])
                        
                                
                        
                        else:
                                close = mktime[1]
                        
                        rightnow = strftime("%H:%M", localtime())
                        if rightnow < strftime("04:00"):
                                right = rightnow.split(":")
                                rightnow = str(str(int(right[0])+24)+":"+right[1])
                        if (close > rightnow > mktime[0]):
                                print("Market ", lisj[2].replace('.db"',''), " is starting at cycle ", cycle)
                                if lisj[1] =='g':
                                	thr.append(_thread.start_new_thread(googlequotemachine.actionking, (a_lock, start1, lisj[0].replace('"',''),database+lisj[2].replace('"',''),0,synamelist,1,0,timetorun) ))
                                elif lisj[1] =='y':
                                        thr.append(_thread.start_new_thread(yahooquotemachine.actionking, (a_lock,start1, lisj[0].replace('"',''),database+lisj[2].replace('"',''),0,synamelist,1,0,timetorun) ))
        
                                else:
                                	thr.append(_thread.start_new_thread(bloombergquotemachine.actionking, (a_lock,start1, lisj[0].replace('"',''),database+lisj[2].replace('"',''),0,) ))
                                time.sleep(0.00001)
        
        print("locks placed and Market engine is running for the....", cycle, " time...with threads",  thr )
        time.sleep(timetorun)
        gc.collect()
        print("locks released and Market engine is restarting for the...", cycle, " time...")
        cycle = cycle + 1
/*email to provide support at vancekingsaxbe@powerdominionenterprise.com, businessaffairs@powerdominionenterprise.com, For donations please write to fundraising@powerdominionenterprise.com*/