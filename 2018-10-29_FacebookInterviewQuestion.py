"""
Author: Danielle Wallace -- github.com/Dewprism
This was a Facebook Technical Interview question I was given on 10/29/2018. 
I failed to resolve the question in time, and decided to complete it as practice.
I'm not sure what the intended solution was! This is just the best I could come up with.
"""

#Given integers a, b, and n, find all positive multiples of a and b up to n.
#Example input: 2, 3, 10
#Example output: 2, 3, 4, 6, 8, 9, 10

a = 3
b = 2
n = 10

#Positive multiples only
if a < 0: a *= -1
if b < 0: b *= -1

high = max(a,b)
low = min(a,b)
highcounter = 1
lowcounter = 1

while highcounter <= n/high:
  highmultiple = high * highcounter
  lowmultiple = low * lowcounter
  if lowmultiple < highmultiple:
    print(lowmultiple)
    lowcounter += 1
  else:
    if lowmultiple == highmultiple: lowcounter += 1
    print(highmultiple)
    highcounter += 1
while lowcounter <= n/low:
  lowmultiple = low * lowcounter
  lowcounter += 1
  print(lowmultiple)
