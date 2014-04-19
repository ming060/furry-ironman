'''
Created on 2014/3/31

@author: YuMing
'''
from uiautomator import Device

def test(obj):
    return obj.fling.horiz

if __name__ == '__main__':
    print 'start'

    d = Device('192.168.185.101:5555')
    
    d(resourceId='com.dropbox.android:id/login_email').set_text('abc')
#     view = d(resourceId='android:id/list')
#     print view.info
#     view.fling.forward()

    print 'end'