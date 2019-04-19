s='s h a k ir'
      
nospaces = [ch for ch in s if ch!=' ']
space = len(s) - len(nospaces) 
  
     
result = ' '*space 
   
result = result + ''.join(nospaces)
print("the result is", result )
  
