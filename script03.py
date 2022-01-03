# -*- coding: utf-8 -*-
import os
import time
import sys

N1 = 0
N2 = 0
R = 0

N1 = float (input('digite o primeiro numero: '))
N2 = float (input('digite o segundo numero: '))


if N2 < N1 : R = N1-N2
else: R = N2-N1


print ( R )
