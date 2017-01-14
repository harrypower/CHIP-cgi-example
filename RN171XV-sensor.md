# Using RN-171-XV Wifly device as automatic sensor IOT
The following are steps to set up the RN-171-XV Wifly device to send its GPIO and its Analog input pins to a web server without a mcu attached!

**Note** the following commands are sent to the Wifly via its uart pins.  This can be done with many methods.  I used a mbed LPC1768 device
programmed to simply pass information it recieved on to the Wifly uart pins.  I used a Tera Term program as the PC terminal program.

**Note** enter command mode with `$$$`

**Note** when in command mode and issuing `save` command the device will now always power up and do the saved settings.  This allows automatic
router connecting and sensor data sending when the below commands are entered and saved!

*Default uart settings to Wifly: Baud 9600, Data 8, Parity none, Stop 1, Flow none*

* *Configure Wifly to connect to router*
  * Following commands issued to Wilfy in command mode!
  ```
  factory RESET
  reboot
  set wlan ssid <my router name>
  set wlan pass <my router password>
  set wlan join 1
  save
  reboot
  ```

  * These commands will now ensure the Wifly will reconnect to your router and get IP address via DHCP from router every time it powers up!

* *Configure Wifly to send sensor data to a web server*
  * Following commands issued to Wilfy in command mode!
    * directly from DS50002230B page 48 of RN171XV user manual!
  ```
  set ip proto 18
  set dns name <your ip address of the chip device on assigned by the router its wifi is connected to>
  set ip host 0
  set ip remote 80
  set com remote GET$/cgi-bin/Gforthmailget.cgi?DATA=
  set q sensor 0xff
  set sys auto 30
  set option format 7
  save
  reboot
  ```

    * These commands will sent the sensor data via a GET message to the web server located at 192.168.0.215
  The port to receive the message is 80.  In this case the cgi script called Gforthmailget.cgi will be executed on the web server.
  Now this will simply return the information that the cgi script normaly returns.  This information will include the QUERY_STRING and it will be something like
  DATA=0D117DF308BF09E909F406DB07CC7AF806A5.  This should be seen on the uart connection of the Tera Term program that was set up to issue the command mode messages.
  The point of this is for testing.  Bellow is another script to retrieve the data from the web server as it receives it so the Tera Term program and the
  mcu will not be needed normally allowing the Wifly to be used with out any other hardware other then the sensors and power circuit!

  * Use the above script to program the Wifly but change the `set com remote` command to say the following:
  ```
  set com remote GET$/cgi-bin/RN171-cgi-get.cgi?DATA=
  ```
    * This will send the GET message every 30 seconds from the Wifly to the server at /cgi-bin/RN171-cgi-get.cgi script for data retrieval and storage example.
