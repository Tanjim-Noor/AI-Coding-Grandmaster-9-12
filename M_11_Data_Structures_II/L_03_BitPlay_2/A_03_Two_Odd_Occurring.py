# Program to find two numbers that are odd occurring

def printTwoOdd(arr, size):

    # xor2 will hold xor of 2 odd occurring numbers
    xorOf2 = arr[0]
    # traverse the array
    for i in range(1, size):
        xorOf2 = xorOf2 ^ arr[i]

    # Set bit = 0
    set_bit = 0

    # This will hold the rightmost set bit from xorOf2
    for i in range(size):
        if(arr[i] & set_bit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

    print("The two ODD elements are : ", x, "&", y)

# Create an empty array
arr = []

# Take array size and elements as input
arr_size = int(input("Enter size of the array : "))
for i in range(0, arr_size):
    z = int(input("Enter element : "))
    arr.append(z)

printTwoOdd(arr, arr_size)
