import time
def decoration_function(func):
    def wrapper_function():
        time.sleep(1)
        print('Wrapper executed this before' )
        func()
        time.sleep(1)  
    return wrapper_function

@decoration_function
def hello_world():
    print("hello_world")
for i in range(5):  
    hello_world()

import os

TEST = os.environ.get('TEST_EMAIL')
print(TEST)