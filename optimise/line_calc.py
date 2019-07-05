#!/usr/bin/python3
import sys, os, time

start = time.time()

f = os.open("poem", os.O_RDONLY)
l = os.read(f, 400).split(b'\n')

le = len(l)
ne = le - l.count(b'')

sys.stdout.write("%d total number of lines\n" % (le))
sys.stdout.write("%d number of empty lines\n" % (le - ne))

avgpl = 0
avgpnl = 0

for i in l:
    l_ = len(i)
    avgpl += l_
    if not i:
        avgpnl += l_

sys.stdout.write("%f avg chars per line\n" % (avgpl/le))
sys.stdout.write("%f avg chars per non empty line\n" % (avgpnl/ne))

t = time.time() - start
with open("res", 'w') as f:
    f.write(str(t))
