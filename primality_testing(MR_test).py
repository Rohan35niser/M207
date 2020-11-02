''' Miller Rabin - a short note 

The Miller-Rabin test picks a random integer 'a' 
which belongs to modulo class of n. 
If the above sequence does not begin with 1, or 
the first member of the sequence that is not 1 is also not -1
then n is not prime.
If n fails the Miller-Rabin test with a sequence starting with 1,
then we have a nontrivial square root of 1 modulo n,
and we can efficiently factor n.                         '''




import random

def square_multiply(x,c,n):
  z=1
  h = list(bin(c))
  del(h[0],h[0])

  for i in range(0,len(h)):
    z = (z**2)%n
    if int(h[i]) ==1:
      z = (z*x)%n
  return(z)

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

  b = square_multiply(a,m,n)

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
print(Miller_Rabin(7433*7919*2649743145))
print(Miller_Rabin(1161163))
print(Miller_Rabin(1178121127*7433*7919*2649743145))




