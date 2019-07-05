import time
start = time.time()
50 / 3
t = time.time()  - start
with open('res', 'w') as f:
    f.write(str(t))
