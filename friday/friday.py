import frida
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Dump payload.')
    parser.add_argument('targets', nargs='+')
    parser.add_argument('--script', '-s', default='virtual.js', help='Path to external JavaScript file')

    args = parser.parse_args()
    pid = frida.spawn(args.targets)
    session = frida.attach(pid)

with open(args.script, 'r') as f:
    script_content = f.read()

script = session.create_script(script_content)
script.load()


script.load()
frida.resume(pid)
sys.stdin.read()
session.detach()

if __name__ == '__main__':
    main()