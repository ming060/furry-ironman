'''
Created on 2014/3/31

@author: YuMing
'''
from uiautomator import device as d

if __name__ == '__main__':
    print 'start'
    
#     print d(text="Settings").wait.exists(timeout=3000)
    # wait until the ui object gone
    #true means the object does not exist
    #false means the object still exist
    print d(text="Settings").wait.gone(timeout=5000)
    
    
    print 'end'