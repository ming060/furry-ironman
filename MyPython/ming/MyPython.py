'''
Created on 2014/3/31

@author: YuMing
'''
from uiautomator import device as d

def test(obj):
    return obj.fling.horiz

if __name__ == '__main__':
    print 'start'

    print d.info
    view = d(resourceId='android:id/list')
    print view.info
    view.fling.forward()
    
    
    print 'end'