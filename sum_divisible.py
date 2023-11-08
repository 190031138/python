''' Given two inputs and first is a number that is divisible and second is sum of digits
You are asked to print smallest number with the following two'''
'''
input1: 13,32
output:8879  where 8+8+7+9 = 32 and divisible by 13

input2:8,22
output:688 where 6+8+8 = 22

constraints < 10 power 6 or 1000000
'''

def sol(a,b):
    for i in range(a,1000000):
        if i % a == 0 and sum(i) == b:
            return i
    


def sum(n): # function to read sum of all the digits
    sum = 0
    while n > 0:
        r = n % 10
        sum += r
        n //= 10  #if we / it will be in float so use // it will eleminate all zeroes
    return sum    #After the sum it will give output 

print(sol(13,32)) #printing the output also sending arguments to function.