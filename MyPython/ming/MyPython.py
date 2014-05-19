# -*- coding: utf-8 -*-
'''
Created on 2014/3/31

@author: YuMing
'''
from uiautomator import Device
import time
import datetime
import os

if __name__ == '__main__':
    print 'start'

#     output_dir = 'C'
#     ts = time.time()
#     st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
#     screenshot_path = '%s%s%s' % (output_dir, os.sep, st)
#     print screenshot_path
    d = Device('HT12ERT00129')
#     d().swipe.left()
#     d(className='android.widget.ImageView').click()
    sdk_version = d.info['sdkInt']
    print sdk_version
    if sdk_version < 18:
        height = d.info['displayHeight']
        d.swipe(1, 1, 1, height - 1, 1)
    else:
        d.open.notification()
#     d.open.notification()
#     d.open.quick_settings()
#     print d(text='Path:').info
#     d.screenshot(screenshot_path)

    print 'end'