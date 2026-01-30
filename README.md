Send CPU & GPU temperatures via python server to Arduino and print them to LCD screen.
Tested with Arduino Mega 2560 and DFRobot LCD Shield. Should also work with any Arduino and LCD screen.
Current python scipt is designed to work with Bazzite Linux, but it also works with e.g. Raspberry Pi / RasPi OS with little modifications.
(RasPi CPU temperature is fetched with /sys/class/thermal/thermal_zone0/temp)

PS. If you want to run the script at boot add #!/usr/bin/env python3 as a first line and create a systemd service.


