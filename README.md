Send CPU & GPU temperatures via python server to Arduino and print them to LCD screen.
Tested with Arduino Mega 2560 and DFRobot LCD Shield. Should also work with any Arduino and LCD screen.
Current python script is designed to work with immutable Fedora, but it should work with other linux/windows too with little modifications.

PS. If you want to run the script at boot add #!/usr/bin/env python3 as a first line and create a systemd service.


