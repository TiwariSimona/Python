s = []
top=none
def isEmpty(stk)
  if(stk==[]):
    return True
  else:
    return false
  
  def push(stk,item)
    stk.append(item)
    top=len(stk)-1
    
 def s_pop(stk)
  if (isEmpty(stk)):
    return('underflow')
  else:
    i=stk.pop()
    if (len(stk)==0):
      top=none
    else:
      top=top-1
   return i

def peek(stk):
  if(isEmpty):
    return('underflow')
  else:
    top=len(stk)-1
    return stk[top]
  
 def display(stk):
  if(isEmpty(stk)):
    print('String is empty!')
  else:
    top=len(stk)-1
    print(stk[top],'<---top')
    for i in range (top-1,-1,-1):
      print (stk[i])
      
      
