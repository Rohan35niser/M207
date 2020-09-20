
''' Euclid's Algorithm for gcd '''

def gcd_euclid(a,b):     
    if a<b:
        (a,b) = (b,a)  #interchange numbers if a<b
    
    while (a%b)!= 0:
        (a,b) = (b,(a%b))    #a becomes b, and b becomes remainder (a%b)      
        
        return b      #iterartes until remainder becomes 0, then returns 'b'


''' EEA = Extended Euclid's Algorithm '''

def EEA(a,b):      
    if b == 0:
        return (1, 0)     # trivial case
    
    else:
        (x, y) = EEA(b, a % b) # recursive call for iteration
        k = a // b

    return (y, x - k * y)   # returns the solution pair


