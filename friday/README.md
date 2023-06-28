- DBI frameworks help with automate analysis
- Install frida import
	- `pip3 install frida-tools`
- friday.py needs to be fed an executable and optionally a dll and optionally a javascript with your choosing of detection
example: `python friday.py something.exe <dll> <-s virtual.js>`



## DBI with Frida-Python
- modified with python bindings
	- python gives us more control over execution and make it easier to troubleshoot issues
- we can make script based of APIs such as VirtualAlloc VirtualProtect
