# Using RN-171-XV Wifly device as automatic sensor IOT
The following are steps to set up the RN-171-XV Wifly device to send its GPIO and its Analog input pins to a web server without a mcu attached!

**Note** the following commands are sent to the Wifly via its uart pins.  This can be done with may methods.  I used a mbed LPC1768 device
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

* *Configure Wifly to send sensor data to a web server*
  * Following commands issued to Wilfy in command mode!
    * directly from DS50002230B page 48 of RN171XV user manual!
  ```
  set ip proto 18
  set dns name 192.168.0.215 \ this should be set to your web server address on the router that Wifly is connected to
  set ip host 0
  set ip remote 80
  set com remote GET$/cgi-bin/Gforthmailget.cgi?DATA=
  set q sensor 0xff
  set sys auto 30
  set option format 7
  save
  reboot
  ```
