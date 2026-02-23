# Space complexity: θ(1), Auxiliary space = θ(1)
def sum(n):
    return n*(n+1)/2

# Linear space
# Space complexity: θ(n), Auxiliary space = θ(1)
def arraysum(a):
    sum=0
    for i in a:
        sum = sum + 1
    
    return(sum)

a = [12, 3, 4, 1]
arraysum(a)

# With the size of the array, the space also required increases.
# Space complexity: θ(n), Auxiliary space = θ(1)

def sum(n):
    if(n<=0):
        return
    return n + sum(n-1)
