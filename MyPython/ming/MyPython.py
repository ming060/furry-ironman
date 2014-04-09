'''
Created on 2014/3/31

@author: YuMing
'''
from uiautomator import device as d

if __name__ == '__main__':
    print 'start'
    
    d.press.home()
    d(description='Apps').click()
    d(text='Apps').click()
    
    
    print 'end'