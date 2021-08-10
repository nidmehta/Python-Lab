#Caching- saves time by storing already used values for a particular function
import time
from functools import lru_cache         #functools is a builtin module

@lru_cache(maxsize = 3)             #maxsize = n stores the last n values of the function call
def abc(num):
    #Function will take atleast  n seconds
    time.sleep(num)
    return num

if __name__ == '__main__':
    print("Start")
    abc(5)              #Value stored
    print("Done")
    abc(5)                  #No delay after using lru decorator
    print("Done Again")