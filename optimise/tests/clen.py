import time
def clen(lst):
	res = 0
	for i in lst:
		res += 1
	return res	

start = time.time()
lis = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
clen(lis)
t = time.time() - start
with open('res', 'w') as f:
	f.write(str(t))
