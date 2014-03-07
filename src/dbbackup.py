/*Owner & Copyrights: Vance King Saxbe. A.*/""" Copyright (c) <2014> Author Vance King Saxbe. A, and contributors Power Dominion Enterprise, Precieux Consulting and other contributors. Modelled, Architected and designed by Vance King Saxbe. A. with the geeks from GoldSax Consulting and GoldSax Technologies email @vsaxbe@yahoo.com. Development teams from Power Dominion Enterprise, Precieux Consulting. Project sponsored by GoldSax Foundation, GoldSax Group and executed by GoldSax Manager."""import sqlite3
from io import StringIO
class dbbackup:
  def dbtransfer(source,destination):
    con = sqlite3.connect(source)
    tempfile = StringIO()
    for line in con.iterdump():
        tempfile.write('%s\n' % line)
    con.close()
    tempfile.seek(0)
    kuk = sqlite3.connect(destination)
    kuk.cursor().executescript(tempfile.read())
    kuk.commit()
    kuk.row_factory = sqlite3.Row
/*email to provide support at vancekingsaxbe@powerdominionenterprise.com, businessaffairs@powerdominionenterprise.com, For donations please write to fundraising@powerdominionenterprise.com*/