# KDB-Project
These two projects were done to improve my KDB skills and demonstrate what I have learned. These were run on my raspberry pi for easy of use 

To use both these demos, you need to have KDB+ installed and set up on the machine you are using. Kdb+ is an in-memory column-oriented database based on the concept of ordered lists. In-memory means it primarily stores its data in RAM. This makes it extremely fast with a much simplified database engine but it requires a lot of RAM (Which no longer poses a problem as servers with massive amounts of RAM are now inexpensive). Column oriented database means that each column of data is stored sequentially in memory

Demo 1: Use IPC with KDB and python to collect data from multiple cryptocurrency exchanges periodically and store in a KDB table and persist at the end of the day.

Instructions to run Demo 1:
1. Start server in the background by calling initServer.sh. This is usually called through crontab every time the pi restarts. 
2. Then call setupServer.py to implement functions and logging in the server. Also done through crontab on reboot.
3. Then call getPrices.py periodically to get prices from exchanges and pass it to server in the background. Called every minute via crontab.
4. Then at the end of the day call saveAndResetKDBServer.py to save partitioned table to reset the q server for new day

Demo 2: Use data collected from demo 1 to demonstrate how websockets can be used to do live charting with the use of HTML, javascript and chartjs

Instructions to run Demo 2:
1. Run the q script tmp.q. This starts a server and sets up web socket functions and logging.
2. Open chartJSBasic.htm in a web browser. Enter the IP address of the device that is running the q server mentioned above and click connect. This should connect the webpage to the server and start receiving data. 
3. Check the webSocketConnections table in the q server to see active connections. 
