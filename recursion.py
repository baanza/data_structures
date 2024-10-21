# recursioning the shit out of life
# SO TUTAANZA NA FACTORIALS
import sys
def factorial(n):
    if n== 0:
        return 1
    else:
        return n * factorial(n- 1)

# Next we do the fibonacci sequence .... A fibonacci sequence is a series in which each number is the sum ofthe preciding two numbers
# It starts with 0 and 1
def fib(n):
    int(n)
    # setting the base case ie for 0 and 1
    if n<= 0:
        return 0
    elif n== 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
# print(fib(int(sys.argv[1])))

# Next on the list is performing the sum of elements in an array
def sum_array(array):
    
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

# print(sum_array([int(i) for i in sys.argv[1:]]))


# next we are gonna try to reverse a string::::

def reverser(s):
    if len(s) == 0:
        return " "
    else:
        return s[-1] + reverser(s[:-1])



# Next we are doing power of numbers
def power(x, n):
    if x== 0:
        return 1
    elif n <0:
        return 1/ power(x, -n)
    else:
        return x * power(x, n-1)
 
if __name__ == "__main__":
    if (sys.argv[1] == "factorial"):
        print(factorial(int(sys.argv[2])))
    elif (sys.argv[1] == "fib"):
        print(fib(int(sys.argv[2])))
    elif(sys.argv[1] == "sum"):
        print(sum_array([int(i) for i in sys.argv[2:]]))
    elif(sys.argv[1] == "reverse"):
        print(reverser(sys.argv[2]))
    elif(sys.argv[1] == "power"):
        print(power(int(sys.argv[2]), int(sys.argv[3])))
    else:
        print('wrong option')


