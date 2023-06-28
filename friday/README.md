- DBI frameworks help with automate analysis
- Install frida import
	- `pip3 install frida-tools`
- friday.py needs to be fed an executable and optionally a dll and optionally a javascript with your choosing of detection
`python friday.py something.exe <dll> <-s virtual.js>`


- with frida-trace, you can quickly intercept APIs of interest
	- `frida-trace -f <target> -i <module Name>!<functions (s) >`
	- example `frida-trace -f run.exe -i KERNEL32.DLL!CreateFile*
	- -f target file to run
	- -i funcgtions to interscept
	- -* wildcard
	- `log('lpText : ' + Memory.readUtf16String(args[1]));` # used as an argument in the handler or even in the python script to get what was passed into the API but exist only in memory 
	- `log('LoadLibraryA(): ' + args[0].readAnsiString());`
- Using it for Crypto example
	- `frida-trace --decorate -f proc.exe -i Crypt*`
		-  `--decorate` will provide the DLL along with the API that's used
```javascript
OnEnter(log, args, state) {
	log('CryptDecrypt()');
	this.decData = args[4];
}

OnLeave(log, retval, state) {
	log('Decrypted data: ' + this.decData.readAnsiString());
}}
```
## DBI with Frida-Python
- modified with python bindings
	- python gives us more control over execution and make it easier to troubleshoot issues
- we can make script based of APIs such as VirtualAlloc VirtualProtect
