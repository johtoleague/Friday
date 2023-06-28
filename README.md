## DBI with Frida-Python
- DBI frameworks help with automated analysis
- Install frida import
	- `pip3 install frida-tools`
- friday.py needs to be fed an executable and optionally a dll and optionally a javascript with your choosing of detection
	- example: `python friday.py something.exe <dll> <-s virtual.js>`
 	  	- Great starting point to dump anything that's allocated or written to allocate space and has an MZ header.
    		- In the javascript, you can change what header you want to look, and modify it to show the hex dump to screen

