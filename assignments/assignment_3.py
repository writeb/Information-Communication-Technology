'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
except:
    print("You didn't put any input when you run your code! Please add an input!")
    input1 = ""

'''
The objective of this assignment is to print either:
    - all information about all dogs in 'all' is given as an input
    - All information about one dog if a dog's name is given as an input.
Several tests will be done with your file with several inputs.
You can find them in the instruction document.
List of installed packages :
    - requests
You cannot use other package than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:

import requests
url = "https://api.thedogapi.com/v1/breeds"
resp = requests.get(url)
df = resp.json()
if input1=='all':
    print (df)
else:
    for i in df:
        if i['name'] == input1:
            print(i)