# create a module lengthconvertor.py 

#lengthconvertor.py
'''conversion between units of length'''

#functions 
def milestokm(n):
  '''Returns the converted length from miles to km'''
  return n*Mtok

def feettoinches(n):
  '''Returns the converted length from feet to inches'''
  return n*FtoI

def inchestofeet(n):
  '''Returns the converted length from inches to feet'''
  return n/FtoI

#constants
MtoK = 1.609344
FtoI = 12
