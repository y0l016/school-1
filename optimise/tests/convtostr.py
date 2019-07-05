import sys, time
start = time.time()
avg = 100; pl = 104
sys.stdout.write(str(avg/pl) + " somehin")
t = time.time() - start
with open('res', 'w') as f:
	f.write(str(t))
