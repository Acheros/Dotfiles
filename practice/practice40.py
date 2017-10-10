#!/usr/bin/python3

tien = int(input("nhap so tien: "))
t500k = 0
t200k = 0
t100k = 0
t50k = 0
t20k = 0
t10k = 0
t5k = 0
t1k = 0


while tien >= 500000:
    tien = tien - 500000
    t500k = t500k + 1
while tien >= 200000:
    tien = tien - 200000
    t200k = t200k + 1
while tien >= 100000:
    tien = tien - 100000
    t100k = t100k + 1
while tien >= 50000:
    tien = tien - 50000
    t50k = t50k + 1
while tien >= 20000:
    tien = tien - 20000
    t20k = t20k + 1
while tien >= 10000:
    tien = tien - 10000
    t10k = t10k + 1
while tien >= 5000:
    tien = tien - 5000
    t5k = t5k + 1
while tien >= 1000:
    tien = tien - 1000
    t1k = t1k + 1


if t500k > 0:
    print("so to 500k la: %i" % t500k)
if t200k > 0:
    print("so to 200k la: %i" % t200k)
if t100k > 0:
    print("so to 100k la: %i" % t100k)
if t50k > 0:
    print("so to 50k la: %i" % t50k)
if t20k > 0:
    print("so to 20k la: %i" % t20k)
if t10k > 0:
    print("so to 10k la: %i" % t10k)
if t5k > 0:
    print("so to 5k la: %i" % t5k)
if t1k > 0:
    print("so to 1k la: %i" % t1k)
