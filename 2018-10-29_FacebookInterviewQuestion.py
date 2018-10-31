"""
Author: Danielle Wallace -- github.com/Dewprism
This was a Facebook Technical Interview question I was given on 10/29/2018. 
I failed to resolve the question in time, and decided to complete it as practice.
I'm not sure what the intended solution was! This is just the best I could come up with.
"""

#Given integers a, b, and n, find all positive multiples of a and b up to n.
#Example input: 2, 3, 10
#Example output: 2, 3, 4, 6, 8, 9, 10

print("a?")
a = int(input())
print("b?")
b = int(input())
print("n?")
n = int(input())

#Positive multiples only
if a < 0: a *= -1
if b < 0: b *= -1

high = highmultiple = max(a,b)
low = lowmultiple = min(a,b)
highcounter = 1
lowcounter = 1

while highcounter <= n/high:
  if lowmultiple < highmultiple:
    print(lowmultiple)
    lowcounter += 1
    lowmultiple = low * lowcounter
  else:
    if lowmultiple == highmultiple: 
      lowcounter += 1
      lowmultiple = low * lowcounter
    print(highmultiple)
    highcounter += 1
    highmultiple = high * highcounter
while lowcounter <= n/low:
  print(lowmultiple)
  lowcounter += 1
  lowmultiple = low * lowcounter
