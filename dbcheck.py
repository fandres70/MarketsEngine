""" Copyright (c) <2014> Author Vance King Saxbe. A, and contributors Power Dominion Enterprise, Precieux Consulting and other contributors. Modelled, Architected and designed by Vance King Saxbe. A. with the geeks from GoldSax Consulting and GoldSax Technologies email @vsaxbe@yahoo.com. Development teams from Power Dominion Enterprise, Precieux Consulting. Project sponsored by GoldSax Foundation, GoldSax Group and executed by GoldSax Manager."""import _thread
import os
import sys
import time
from src import googlequotemachine
from src import yahooquotemachine
from src import bloombergquotemachine
from src import createtablesgooglefinance
from src import createtablesyahoofinance
from src import createtablesbloomberg

start1 = []

sys.setrecursionlimit(100000)
database = "data/"

with open('conf/urls.conf') as f:
    actionlist = f.read().splitlines()



for listo in actionlist:
        lis = listo.split('", "')
        if lis[1] =='g':
               
                createtablesgooglefinance.createtables(lis[0].replace('"',''), database+lis[2].replace('"',''))
        elif lis[1]=='y':
              	createtablesyahoofinance.createtables(lis[0].replace('"',''), database+lis[2].replace('"',''))
        else:
               	createtablesbloomberg.createtables(lis[0].replace('"',''), database+lis[2].replace('"',''))
