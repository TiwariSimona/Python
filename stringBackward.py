# write a program to print a string backwards

#iteration
S = 'simona'
L = len(S)
for i in range (L-1,-1, -1):
  print (S[i], end = ' ')
  
#Recursion
S = 'simona'
def rev(S):
  if (len(S)==0):
    return S
  else:
    return ( S[1: ])+S[0]
 


#Recursion2
def rev(s):'suchismita'
	if(len(s)==0):
		return 1
		else:
			return rev(s[1:])+s[0]
