import argparse
from ampy import files,pyboard
import os

parser=argparse.ArgumentParser()
parser.add_argument("action",type=str,help="sync -- get files from board\npush --push code to board")
parser.add_argument('-d','--device', default='COM3', help='the serial device of the pyboard')
args=parser.parse_args()
device=args.device
fs=files.Files(pyboard.Pyboard(device))

def sync():
    try:
        os.mkdir("scripts")
    except:
        pass
    fns=fs.ls(long_format=False)
    for fn in fns:
        with open(f"scripts/{fn}","wb") as f:
            f.write(fs.get(fn))
    

def push():
    for fn in os.listdir("scripts"):
        with open(f"scripts/{fn}","rb") as f:
            fs.put(fn,f.read())

if __name__=="__main__":
    func={"sync":sync,"push":push}[args.action]
    func()