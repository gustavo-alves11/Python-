import os
import sys 
import time

total = 0
a= 0
b= 0
a= int(input('digite o numero inicial: '))
b= int(input('digite o numero final: '))

for i in range ( a, b ):      
    if i%2!=0:         
        total+= i
print(total)
