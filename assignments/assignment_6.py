'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
except:
    print("You didn't put any input when you run your code! Please add an input!")
    input1 = ""
    input2 = ""


'''
The objective of this assignment is to print the expected output.
You can find it in the instruction folder.
List of installed and authorized packages :
    - numpy
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
import numpy
input1 = [int(i) if i.isdigit() else i for i in input1.split(',')]
# for i in input1.split(','):
#     if i.isdigit():
#         input1.append(int(i))
#     else :
#         input1.append(i)
input2 = [int(i) if i.isdigit() else i for i in input2.split(',')]
# for i in input2.split(','):
#     if i.isdigit():
#         input2.append(int(i))
#     else :
#         input2.append(i)


arr = numpy.array([input1, input2])

print(arr.T)