import time
start = time.time()
lis = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
#lis.__len__
len(lis)
t = time.time() - start
with open('res', 'w') as f:
	f.write(str(t))
