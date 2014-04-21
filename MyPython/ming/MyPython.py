'''
Created on 2014/3/31

@author: YuMing
'''
from uiautomator import Device

def test(obj):
    return obj.fling.horiz

if __name__ == '__main__':
    print 'start'

    d = Device()
    
    d(resourceId='com.android.launcher3:id/apps_customize_pane_content').swipe.left()
#     view = d(resourceId='android:id/list')
#     print view.info
#     view.fling.forward()

    print 'end'