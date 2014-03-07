/*Owner & Copyrights: Vance King Saxbe. A.*/""" Copyright (c) <2014> Author Vance King Saxbe. A, and contributors Power Dominion Enterprise, Precieux Consulting and other contributors. Modelled, Architected and designed by Vance King Saxbe. A. with the geeks from GoldSax Consulting and GoldSax Technologies email @vsaxbe@yahoo.com. Development teams from Power Dominion Enterprise, Precieux Consulting. Project sponsored by GoldSax Foundation, GoldSax Group and executed by GoldSax Manager."""#!/usr/bin/env python3
import _thread
import os
import sys
from src/googlequotemachine import getquote
from yahooquotemachine import getquote
from bloombergquotemachine import getquote
from createtablesgooglefinance import createtable
from createtablesyahoofinance import createtable
from createtablesbloomberg import createtable

start1 = []


sys.setrecursionlimit(100000)



with open('/conf/urls.conf') as f:
    actionlist = f.read().splitlines()



for listo in actionlist:
	lis = listo.split(",")
	if lis[1] =='g':
		createtablesgooglefinance.createtable(lis[0], lis[1], lis[2])
	elif lis[1]=='y':
    		createtablesyahoofinance.createtable(lis[0], lis[1], lis[2])
	else:
   		createtablesbloomberg.createtable(lis[0], lis[1], lis[2])

a_lock = _thread.allocate_lock()
thr = []
with a_lock:
        print("locks placed and engine is running.....")

        for listo in actionlist:
		lis = listo.split(",")
		if lis[1] =='g':
                	thr.append(_thread.start_new_thread(googlequotemachine.getquote, (lis[0],lis[1],lis[2],) ))
		elif lis[1] =='y':
                	thr.append(_thread.start_new_thread(yahooquotemachine.getquote, (lis[0],lis[1],lis[2],) ))

		else:
                	thr.append(_thread.start_new_thread(bloombergquotemachine.getquote, (lis[0],lis[1],lis[2],) ))

while 1:
        pass
for th in thr:
        th._thread.exit()

/*email to provide support at vancekingsaxbe@powerdominionenterprise.com, businessaffairs@powerdominionenterprise.com, For donations please write to fundraising@powerdominionenterprise.com*/