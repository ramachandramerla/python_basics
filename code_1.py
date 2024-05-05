import sys
from python_basics import goodbye
from python_basics import hello

if len(sys.argv)==2:
    hello(sys.argv[1])
else:
    goodbye(sys.argv[1])