import time
start = time.time()
ts = 1
ts = ts + 1
t = time.time()  - start
with open('res', 'w') as f:
    f.write(str(t))
