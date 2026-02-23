# For function1, the Algorithm goes like this:
# (4*5) / 2

# So, the number of iterations will be 1.

# For function2 the Algorithm goes like:
# 1 + 2 + 3 + 4

# So number of iterations will be 1 + 1 + 1 + 1 = 4 = n(input) iterations

# For function3 the Algorithm goes like:
# 1 + (1+1) + (1+1+1) + (1+1+1+1)

# So number of iterations will be 1 + 2 + 3 + 4 = 10

# So for our functions 1,2 and 3, the number of iterations will depend upon n (4 in our case):
# 1. Fun1 : (C1)
# 2. Fun2 : (C2(n) + C3())
# 3. Fun3: ((C4(n^2)) + C5(n) + C6())

# The above conversions are known as the Asymptotic analysis of the algorithm.

# Comparison between function1 and function2 :
# func1 is O(1) - Constant time
# func2 is O(n) - Linear time
# func3 is O(n^2) - Quadratic time
