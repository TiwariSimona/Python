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
      
print('Stack Implementation') 
print('1.push')
print('2.pop')
print('3.peek')
print('4.Display')
print('5.Exit')
 
ch=int(input('Enter the choice between 1 and 5')
  if (ch==1):
       item = (input('Enter the item you want to push'))
       push(5,item)
       print('% added successfully ' %item)
       input('Press any key to continue')
  elif(ch==2):
       item=s_pop(s)
       if (item=='underflow):
           print('underflow!stack is empty')
       else:
           print('%d is popped' %item)
       input('Press any key to continue')
  elif(ch==3):
           item==peek(s)
           if (item=='underflow'):
            print ('Underflow!Stack is empty')
           else:
            print('%d is at the top'%item)
           input ('Press any key to continue')
   elif(ch==4):
           display(s)
           input('Press any to continue')
   elif(ch==5):
           break
   else:
           print('Enter between 1 & 5')
           input('Press any to continue')
  print('/n/n/n')
           
           
    
      
      
