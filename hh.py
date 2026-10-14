def palindrome(n):
  i=0
  j=len(n)-1
  while(i<j):
    if n[i]== n[j]:
      i=i+1
      j=j-1
      return True
    else:
      return False
      
print(palindrome("radar"))