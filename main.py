#title           :main.py
#Project         :Multithreading
#description     :Multiplies 2 matrices that are randomly gen. and speeds up using multithreading
#Author          :Michael Lawson (lawsmichael@gmail.com)
#Date            :10/5/14
#Version         :0.0
#usage           :python main.py (int m) (int n)
#notes           :m would be the size of the matrices is and n is the number of threads generated

from __future__ import print_function
from multiprocessing.pool import ThreadPool
import numpy
import sys

#[[randint[0,9] for _ in xrange(10)] for __ in xrange(1)]
class newthread:
    def __init__(self, A, B, C, m):
        self.A = A
        self.B = B
        self.C = C
        self.m = m
    def calculate(self, part1, part2):
        for x in range(part1, part2):
            for y in range(self.m):
                for z in range(self.m):
                    C[x][y] += A[x][z] *B[z][y]
        return C
    '''
    print (part1)
    print (part2)
    print (range(part1, part2))
    '''



m = int(sys.argv[1])
n = int(sys.argv[2])
pool = ThreadPool(processes=n)

if not(m>n):
    exit("Matrix size isn't bigger than threads")

if not((m%n)==0):
    exit("Treads don't divide into matrices evenly")
A = numpy.ctypeslib.array(numpy.random.randint(10, size=(m,m)))
B = numpy.ctypeslib.array(numpy.random.randint(10, size=(m,m)))
C = numpy.ctypeslib.array(numpy.zeros((m,m)))
'''
A = numpy.zeros((m,m))
B = numpy.zeros((m,m))
C = numpy.zeros((m,m))
for x in range(m):
    for y in range(m):
        A[x,y] = randint(0, 10)
        B[x,y] = randint(0, 10)
'''

#print ("should be %"% C)
thread = []
f3=open('C.txt', 'w+')
w = 0
a = newthread(A, B, C, m)
while w < n:
    thread.append([])
    thread[w] = pool.apply_async(a.calculate, args=(((w*m)/n), (((w+1)*m)/n)))
    #thread[x].start()
    #print (x)
    w = w + 1
for x in range(n):
    C = thread[x].get()
'''
thread.append([])
thread[0] = pool.apply_async(newthread, args=(0/n, (m), A, B, C))
'''
'''
while ((count+1) < n):
    thread.append(newthread((count*m)/n, ((count+1)*m)/n, A, B, C))
    thread[count].start()
    #thread[count].join()
    count = count +1

for x in thread:
    thread[x].start()
'''
'''
f1=open('A.txt', 'w+')
f2=open('B.txt', 'w+')
print (A, file=f1)
print (B, file = f2)
print (C, file=f3)
f1.close()
f2.close()
f3.close()
'''

numpy.savetxt('A.txt', A)
numpy.savetxt('B.txt', B)
numpy.savetxt('C.txt', C)