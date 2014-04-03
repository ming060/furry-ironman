# -*- coding: utf-8 -*-
from robot.api import logger
from uiautomator import Device

class Mobile():

    def __init__(self, serial_number):
        self.device = Device(serial_number)

    def print_info(self):
        logger.info('Device info: %s' % self.device.info)

    def get_object(self,**stuff):
        return self.device(**stuff)

    def get_info_of_object(self, obj):
        return obj.info

    def press_power(self):
        self.device.press.power()

    def press_home(self):
        self.device.press.home()

    def click(self, **stuff):
        self.device(**stuff).click()

    def call(self, obj, method, **stuff):
        func = getattr(obj, method)
        return func(**stuff)

if __name__ == '__main__':
    print 'start'

    m = Mobile('HYZPLVR48T6TS8LV')
    linearLayout = m.get_object(className='android.widget.LinearLayout', index=2)
    info_dict = m.get_info_of_object(linearLayout)
    print info_dict
    print info_dict['chileCount']
    chileCount = int(info_dict['chileCount']) - 1
    print chileCount
    btn = m.call(linearLayout, 'child', instance=chileCount, className='android.widget.ImageView')
    m.call(btn, 'click')

    print 'end'