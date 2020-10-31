import random

def modulo(b,e,n):
  i=1
  a=b
  while i<e:
    a=(b*a)%n
    i+=1
  return a

def Miller_Rabin(n):
  a = random.randint(1,n)
  if n%2 != 0:
    m = (n-1)//2
    k = 1
    while m%2==0:
      m = m//2
      k = k+1
  else:
    m = n-1
    k = 0

  b = modulo(a,m,n)

  if b%n == 1:
    return("n is prime")

  for i in range(0,k):
    if b%n == n-1:
      return("n is prime")
    else:
      b = (b**2)%n
  return("n is composite")

print(Miller_Rabin(29))
print(Miller_Rabin(565))
print(Miller_Rabin(7433))




