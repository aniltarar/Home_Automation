# Home_Automation
Home automation system running on Local Area Network on a Web Server using Flask. 

home_automation.py starts the web server running on Raspberry Pi 4/4GB. Two 5V relays and a DHT11 temperature and humiditiy sensor 
are connected an Arduino Uno and communication with the Raspberry Pi via Serial Communication. Relays are connected to a lamp and 
a heater which can be turned on or off via any device connected to the Local Area Network via web browser app.

In addition the index.html page 
(main page) shows the real life weather temperature of Sydney trhough openweathermap API.
