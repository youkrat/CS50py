import sys 
from sayings import hello

if len(sys.argv)!=2:
    sys.exit
else:
    hello(sys.argv[1])