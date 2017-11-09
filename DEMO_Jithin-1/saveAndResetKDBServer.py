#!/usr/bin/python
import qpython.qconnection as qconnection

q=qconnection.QConnection(host = 'localhost', port = 5001)

try:
    q.open()
    q('saveTable[]') #save all data in tbl to partitioned db
    q('tbl:([]date:();time:();sym:();exch:();price:())') #reset tbl to be empty
finally:
    q.close()
