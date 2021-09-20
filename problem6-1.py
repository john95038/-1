# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 23:08:44 2021

@author: 羅傳郡
"""
import gmpy2
from gmpy2 import mpz, gcd

import time
import random

start = time.time()

# generate the key-----------------------------------------------

rs = gmpy2.random_state(hash(gmpy2.random_state()))
P = gmpy2.mpz_urandomb(rs, mpz('50'))
P = gmpy2.next_prime(P)
print("P =", P)

Q = gmpy2.mpz_urandomb(rs, mpz('50'))
Q = gmpy2.next_prime(Q)
print("Q =", Q)

n = P*Q
print("n =", n)


#-----------------------------------------------------------------


#print(gmpy2.is_prime(125778791843321 ))

#n = mpz(63281217910257742583918406571)
         #202820047517886565433833121
         #1818839519097939557366384701307
x = mpz(2)
y = x**2 + 1


for i in range(n):
    p = gcd(y-x,n)
    if p != 1:
        print(p)
        break
    else:
        y=(((y**2+1)%n)**2+1)%n
        x=(x**2+1)%n


end = time.time()        
print(n//p,'\n')
print("total time：", end-start, "s")


'''
63281217910257742583918406571 = 503115167373251 * 125778791843321
'''