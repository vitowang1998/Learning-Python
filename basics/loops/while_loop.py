# while loop in Python

# example 1
'''
while True:
    print('hello')
'''
# control-C: force the program to stop

# example 2: print a string and strip off its first char every time
myString = 'hello'
while myString:
    print(myString, end = '-> ')
    myString = myString[1:]
