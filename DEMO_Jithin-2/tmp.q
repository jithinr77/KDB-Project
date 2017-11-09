\p 5000
\l partitionedTable

webSocketConnections:([handle:()];ipAddress:();connectedTime:();disconnectedTime:())

sampletable2:20#select time, price from crytoMarketPrice where date=2017.10.27,sym=`ETHUSD,exch=`KRAK

logHandle:neg hopen`:/home/pi/usbdrv/DEMO_Jithin/stdAudit.log
logWrite:{[para]logHandle para;}
logWrite[(string .z.p)," [VERBOSE] Connected to Logging File"]

//When Connection opens, add it to the webSocketConnections table
.z.wo:{
	show `opening;
	show ipAddress:"." sv string"h"$0x0 vs .z.a;
	show userName: .z.u;
	show handle:.z.w;
	show count (.z.w; .z.u;enlist "." sv string 256 vs .z.a)
	show `webSocketConnections upsert (handle;ipAddress;.z.p;0Np);
	{neg[x] "{ \"tbl\":",(.j.j sampletable2),"}"} .z.w;
	logWrite[(string .z.p)," [INFO] .z.wo Connection opened on handle: ", string[handle], " for ipAddress: ", ipAddress];
	/ show (string .z.p),"[INFO] Connection opened on handle: ", string[handle], " for ipAddress: ", ipAddress
 }

//When Connection closes, make changes to the webSocketConnections table
.z.wc:{
	show `closing;
	show x;
	/ delete from `webSocketConnections where handle=x
	update disconnectedTime:.z.p from `webSocketConnections where handle=x;
	logWrite[(string .z.p)," [INFO] .z.wc Connection closed for handle: ", string x ];
 }

.z.ts:{
	dataToSend::select from sampletable2 where i=first 1?count[sampletable2];
	{neg[x] "{ \"tbl\":",(.j.j dataToSend),"}";
		logWrite[(string .z.p)," [INFO] .z.ts data send to websocket: ",string x];
	 } each exec handle from webSocketConnections where disconnectedTime=0Np;
 }

\t 1000