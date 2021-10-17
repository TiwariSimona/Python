# write a program to print a string backwards

#iteration
S = 'simona'
L = len(S)
for i in range (L-1,-1, -1):
  print (S[i], end = ' ')
  
#Recursion
def rev(s):'suchismita'
	if(len(s)==0):
		return 1
	else:
		return rev(s[1:])+s[0]
