## DBI with Frida-Python
- DBI frameworks help with automated analysis
- Install frida import
	- `pip3 install frida-tools`
- friday.py needs to be fed an executable and optionally a dll and optionally a javascript with your choosing of detection
example: `python friday.py something.exe <dll> <-s virtual.js>`




- we can make script based of APIs such as VirtualAlloc VirtualProtect
