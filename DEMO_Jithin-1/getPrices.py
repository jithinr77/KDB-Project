#!/usr/bin/python
import sys, json, csv;
from collections import OrderedDict;
from six.moves import urllib;

import qpython.qconnection as qconnection

#ETH-USD-GDAX
ethGdaxQuery='https://api.gdax.com/products/ETH-USD/book'
ethGdaxResult=urllib.request.urlopen(ethGdaxQuery).read()
obj=json.loads(ethGdaxResult,object_pairs_hook=OrderedDict)
print "ethGdaxPrice:"+ obj["bids"][0][0]
ethGdaxPrice=obj["bids"][0][0].encode('utf-8')

#BTC-USD-GDAX
btcGdaxQuery='https://api.gdax.com/products/BTC-USD/book'
btcGdaxResult=urllib.request.urlopen(btcGdaxQuery).read()
obj=json.loads(btcGdaxResult,object_pairs_hook=OrderedDict)
print "btcGdaxPrice:"+ obj["bids"][0][0]
btcGdaxPrice=obj["bids"][0][0].encode('utf-8')

#ETH-USD-KRAK ETH-EUR-KRAK BTC-USD-KRAK BTC-EUR-KRAK
krakQuery='https://api.kraken.com/0/public/Ticker?pair=ETHUSD,ETHEUR,XBTUSD,XBTEUR'
krakResult=urllib.request.urlopen(krakQuery).read()
obj=json.loads(krakResult,object_pairs_hook=OrderedDict)
ethUsdKrakPrice=obj["result"]["XETHZUSD"]["a"][0].encode('utf-8')
btcUsdKrakPrice=obj["result"]["XXBTZUSD"]["a"][0].encode('utf-8')
ethEurKrakPrice=obj["result"]["XETHZEUR"]["a"][0].encode('utf-8')
btcEurKrakPrice=obj["result"]["XXBTZEUR"]["a"][0].encode('utf-8')

#create connector instance with port 5001
q=qconnection.QConnection(host = 'localhost', port = 5001)
try:
    q.open() #open connection to q
    q('{`tbl insert (.z.d;.z.n;`ETHUSD;`GDAX;"F"$x)}',ethGdaxPrice)
    q('{`tbl insert (.z.d;.z.n;`BTCUSD;`GDAX;"F"$x)}',btcGdaxPrice)
    q('{`tbl insert (.z.d;.z.n;`ETHUSD;`KRAK;"F"$x)}',ethUsdKrakPrice)
    q('{`tbl insert (.z.d;.z.n;`BTCUSD;`KRAK;"F"$x)}',btcUsdKrakPrice)
    q('{`tbl insert (.z.d;.z.n;`ETHEUR;`KRAK;"F"$x)}',ethEurKrakPrice)
    q('{`tbl insert (.z.d;.z.n;`BTCEUR;`KRAK;"F"$x)}',btcEurKrakPrice)

finally:
    q.close()
