# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy


n, m = map(int, input().split())
a = numpy.array([list(map(int, input().split())) for _ in range(n)])


b = numpy.array([list(map(int, input().split())) for _ in range(n)])

if a.shape == b.shape:
    print(a + b)
    

    print(a - b)
    

    print(a * b)
    
    print(numpy.floor_divide(a, b))

    print (a % b)
    
    print (a**b)

    # ///

    # Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')

A = numpy.array(input().split(), float)

print (numpy.floor(A) )       
print (numpy.ceil(A))
print (numpy.rint(A))                