import pandas
import pyarrow
import numpy as np
import sklearn.preprocessing as skprepro
'''
-------------------------ENDTERM EXAM-----------------
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
except:
    pass
'''
In the following file, do not delete anything (comments, code, ...). Just add you code in every part (one per exercise).
Use my variable for input (if there is any), use my printing for output (if there is any).
You can upload your code to codepost.io to check the tests. A sucess in one test doesn't always mean than your exercise is correct,
a fail doesn't always mean that your exercise is wrong. I will check all codes.
At the end of exam, you should upload the last version of your code to codepost.io or to the online folder on Teams.
The only authorized packages are:
- pandas
- pyarrow
- fastparquet
- numpy
- sklearn
- matplotlib
- datetime

'''

if input1 == '3':
# ----------------------EXERCISE 3 - Machine Learning I--------------------------------------
# Instructions:
# - Transform all the three given lists into numpy arrays.
# - Transform the L1 array into a matrix (called L5) with 10 lines and 2 columns.
# - Print the obtained matrix (L5). You can find a example of the desired matrix in the document Ex_3_array_new_shape_V5.txt
# - Reshape the arrays L2 and L3 into 1 columns arrays and create a 2 columns matrix  (called L6) where the first column is the L2 array and the second the L3 array.
# - Print the obtained matrix (L6). You can find a example of the desired matrix in the document Ex_3_array_matrix_V5.txt
# - Do the addition of L1 to L2 and call it L7.
# - Print the obtained array (L7). You can find a example of the desired matrix in the document Ex_3_array_operation_V5.txt

    L1 = [55, 36, 28, 23, 9, 39, 52, 13, 19, 6, 39, 1, 44, 15, 36, 36, 15, 8, 16, 41]
    L2 = [8, 12, 35, 55, 55, 11, 37, 35, 48, 48, 26, 43, 45, 26, 3, 28, 17, 36, 22, 12]
    L3 = [54, 3, 36, 4, 8, 54, 19, 8, 22, 29, 32, 24, 6, 22, 39, 15, 26, 22, 28, 32]

    arrL1 = np.array(L1).reshape(-1, 1)
    arrL2 = np.array(L2).reshape(-1, 1)
    arrL3 = np.array(L3).reshape(-1, 1)

    L5 = arrL1.reshape(10, 2)

    L6 = np.hstack((arrL2, arrL3))

    L7 = L1 + L2
    # Here are the print function for each matrix:
    print(L5)
    print(L6)
    print(L7)
# ----------------------End of EXERCISE 3 --------------------------------------
elif input1 == '5':
# ----------------------EXERCISE 5 - Machine Learning III--------------------------------------
# Instructions:
# You have one feature. You objective is to transform it into a matrix for a polynomial regression  of degree 4.
# In the matrix, the first column is the feature, the second : the feature power 2, ... until power 4.
# You can find an example of the desired matrix in the document Ex_5_poly_matrix_V5.txt

    feature = [-657, -254, -798, -237, -319, 170, -58, -651, 1, 29, -58, -738, 36, -98, 406, -842, -285, -963, -789, -326, -439, 413, 373, -512, -78, 110, -556, -386, -41, -112]

    poly4 = skprepro.PolynomialFeatures(degree = 4, include_bias=False)

    x_polymial = poly4.fit_transform(np.array(feature).reshape(-1, 1))







# Here is the print instructions to print the polynomial matrix rounded.
    print(np.around(x_polymial,3))

# ----------------------End of EXERCISE 5 --------------------------------------