import time
start = time.time()
def div(fn, ln):
    i, quotient, remainder = 0, 0, 0
    for i in range(31, -1, -1):
        quotient <<= 1
        remainder <<= 1
        remainder |= (fn & (1 << i)) >> i

        if remainder >= ln:
            remainder -=  ln
            quotient |= 1
    return quotient
div(50, 3)
t = time.time() - start
with open('res', 'w') as f:
    f.write(str(t))
