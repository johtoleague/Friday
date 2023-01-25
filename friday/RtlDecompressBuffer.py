import frida
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Dump payload.')
    parser.add_argument('targets', nargs='+')
    args = parser.parse_args()

    pid = frida.spawn(args.targets)
    session = frida.attach(pid)

    script = session.create_script("""
 try {
            Module.load('KERNEL32.DLL');
            Module.load('NTDLL.DLL');
        } catch (err) {
            console.log(err);
        }
        try {
            var vaExportAddress = Module.getExportByName("NTDLL.DLL", "RtlDecompressBuffer");
        } catch (err) {
            console.log(err);
        }
     
        Interceptor.attach(vpExportAddress, 
        {   
            onEnter: function (args){
                var vpAddress = args[1];
                var vpSize = args[2].toInt32();
                console.log("\\nTtlDecompress called!");
                console.log("\\tAddress: " + vpAddress);
                console.log("\\tSize: " + vpSize);
                console.log("\\n" + hexdump(vpAddress));
                if (vpAddress.readAnsiString(2) != "MZ"){
                    var someBinData = vpAddress.readByteArray(vpSize);
                    var filename = vpAddress +"_mz.bin";
                    var file = new File(filename, "wb");        
                    file.write(someBinData);
                    file.flush();
                    file.close();
                    console.log("\\nDumped file: " + filename);
                }
            }
        });
            
    """)
    script.load()
    frida.resume(pid)
    sys.stdin.read()
    session.detach()

if __name__ == '__main__':
    main()
