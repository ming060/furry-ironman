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
    d = Device('0489902425228ab9')
#     d().swipe.left()
#     d(className='android.widget.ImageView').click()
    print d(textStartsWith='Path').info
#     print d(text='Path:').info
#     d.screenshot(screenshot_path)

    print 'end'