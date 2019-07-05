import sys
import time

def custom_print(*string, sep=' ', end='\n'):
    last = len(string) - 1
    for n, i in enumerate(string):
        sys.stdout.write(i)
        if n != last:
            sys.stdout.write(sep)
    sys.stdout.write(end)

#start = time.time()
#custom_print("lol", "lmao")
#t = time.time() - start
#print(t)
#start = time.time()
#print("lol", "lmao")
#t = time.time() - start
#print(t)
