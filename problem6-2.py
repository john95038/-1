# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 04:00:49 2021

@author: 羅傳郡
"""

import gmpy2
from gmpy2 import mpz, gcd

import time
import random


def check_dc_brute(g,x,p):
    temp = mpz(1)
    while x > 0:
        temp = temp * g % p
        x = x-1
        
    return temp
        





rs = gmpy2.random_state(hash(gmpy2.random_state()))

p = gmpy2.mpz_urandomb(rs, mpz('60'))
p = gmpy2.next_prime(p)
print("P = ", p)

g = 2
#gmpy2.mpz_random  (rs, p)
print("g = ", g)

ans_x = gmpy2.mpz_random(rs, p-1) % 10000 + 1
print("ans_x = ", ans_x)

y = check_dc_brute(g,ans_x,p)
print("y = ", y)

print("\ny = g ** ans_x mod p \n")






start = time.time()

x = 1
while x < p:
    if check_dc_brute(g,x,p) == y:
        print("Discrete Log found, x = ", x)
        break
    x = x+1


end = time.time()        


print("total time：", end-start, "s")
