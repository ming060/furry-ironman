'''
Created on 2014/3/31

@author: YuMing
'''
from uiautomator import Device

def test(d, name, dict1, *dicts):
#     d.watchers.run()
    watcher = d.watcher(name)
    for dict in dicts:
        watcher.when(**dict)
    watcher.click(**dict1)
    d.watchers.run()
#     d.watcher('AUTO_CLICK_TEXT_WHEN_TEXT_EXISTENCE').when(**dicts[0]).when(**dicts[1]).click(**dict)
#     d.watcher('AUTO_CLICK_TEXT_WHEN_TEXT_EXISTENCE').when(text='Taipei City').click(text='Apps')

class a(object):
    def f(self, text):
        print text
        return self

if __name__ == '__main__':
    print 'start'
    
#     a=a()
#     a.f('a').f('b')

    d = Device('0489902425228ab9')
    b_dict = {'text': 'Apps', 'clickable': True}
    a_dict = {'text': 'CookieRun'}
    c_dict = {'resourceId': 'com.android.deskclock:id/analog_appwidget'}
    test(d, 'a',b_dict, a_dict, c_dict)
#     d.watcher('AUTO_CLICK_TEXT_WHEN_TEXT_EXISTENCE').when(**dicts[0]).when(**dicts[1]).click(**dict)
#     w = d.watcher('a')

#     w = d.watcher('AUTO_CLICK_TEXT_WHEN_TEXT_EXISTENCE')
#     w.when(resourceId='com.android.deskclock:id/analog_appwidget')
#     w.when(text='CookieRun')
#     w.click(text='Apps')
#     d.watchers.run()
#     print d.watcher('AUTO_CLICK_TEXT_WHEN_TEXT_EXISTENCE').triggered
#     print d.watchers

#     ball = d(resourceId='com.facebook.orca:id/url_image_image')
#     bound = ball.info['visibleBounds']
#     top = bound['top']
#     left = bound['left']
#     right = bound['right']
#     bottom = bound['bottom']
#     d.swipe(963, 192, 550, 1620, steps=10)
#     u'visibleBounds': {u'top': 99, u'left': 870, u'right': 1056, u'bottom': 285}}
# 547 1620
#     view = d(resourceId='android:id/list')
#     print view.info
#     view.fling.forward()

    print 'end'