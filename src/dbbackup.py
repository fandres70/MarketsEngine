import sqlite3
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
