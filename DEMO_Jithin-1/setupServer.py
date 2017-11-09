#!/usr/bin/python
import qpython.qconnection as qconnection


q=qconnection.QConnection(host = 'localhost', port = 5001)
try:
    q.open()
    q('testVar1:`jithinWasHere')
    q('logHandle:neg hopen`:/home/pi/usbdrv/DEMO_Jithin2/stdAudit.log')
    q('logWrite:{[para]logHandle para;}')
    q('logWrite[(string .z.p)," setupServer script loaded by ",string .z.u]')

    #SETUP shimming/logging functionality
	# Authentication
    q('.z.pw:{[user;pass]logText:(string .z.p), " .z.pw Connection request(" ,(string .z.w) ,") from: " ,string[user], " using password:" , pass; logWrite[logText];1b}')
    # Connection opened
    q('.z.po:{[handle]logText:(string .z.P), " .z.po Connection:",string[.z.w]," opened by ",string .z.u;logWrite[logText]}')
    # Connection closed
    q('.z.pc:{[oldhandle]logText:(string .z.P), " .z.pc Connection closed for handle:",string oldhandle;logWrite[logText];-1}')

    q('tbl:([]date:();time:();sym:();exch:();price:())') #create empty table

    #function to save table as partition
    q('saveTable:{[]{[dte](`$":/home/pi/usbdrv/Script/pythonKDB/partitionedTable/",string[dte],"/crytoMarketPrice/")set @[;`sym;`p#]`sym xasc delete date from .Q.en[`:/home/pi/usbdrv/Script/pythonKDB/partitionedTable/]select from tbl where date=dte}each distinct tbl.date}')


finally:
    q.close()