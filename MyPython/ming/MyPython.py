'''
Created on 2014/3/31

@author: YuMing
'''
from uiautomator import Device

def test(obj):
    return obj.fling.horiz

if __name__ == '__main__':
    print 'start'

    d = Device('0489902425228ab9')
    
    ball = d(resourceId='com.facebook.orca:id/url_image_image')
    bound = ball.info['visibleBounds']
    top = bound['top']
    left = bound['left']
    right = bound['right']
    bottom = bound['bottom']
    d.swipe(963, 192, 550, 1620, steps=10)
#     u'visibleBounds': {u'top': 99, u'left': 870, u'right': 1056, u'bottom': 285}}
# 547 1620
#     view = d(resourceId='android:id/list')
#     print view.info
#     view.fling.forward()

    print 'end'