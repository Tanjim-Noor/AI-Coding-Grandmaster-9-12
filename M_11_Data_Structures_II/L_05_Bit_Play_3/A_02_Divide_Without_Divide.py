# Program to divide two numbers without using the division operator

def divide(quoDividend, aurDivisor):

    # Check if divisor is +ve or -ve
    sign = -1 if((quoDividend < 0) ^ (aurDivisor < 0)) else 1;

    # Make both positive
    aurDividend = abs(quoDividend);
    aurDivisor = abs(aurDivisor);

    quotientNumber = 0
    tempNumber = 0

    # Go from 31 to 0 and accumulate all valid bits
    for i in range(31, -1, -1):
        if(tempNumber + (aurDivisor << i) <= aurDividend):
            tempNumber += aurDivisor << i
            quotientNumber |= 1 << i

    # Assuming the sign value computed earlier is -1, negate the quotient value
    if (sign == -1):
        quotientNumber = -quotientNumber

    return quotientNumber

a = int(input("Enter a for a/b : "))
b = int(input("Enter b for a/b : "))
print("Result of ",a,"/",b," is :",divide(a, b))
