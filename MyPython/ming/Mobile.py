# -*- coding: utf-8 -*-
from robot.api import logger
from uiautomator import Device

def run_async(func):
    """
        run_async(func)
            function decorator, intended to make "func" run in a separate
            thread (asynchronously).
            Returns the created Thread object

            E.g.:
            @run_async
            def task1():
                do_something

            @run_async
            def task2():
                do_something_too

            t1 = task1()
            t2 = task2()
            ...
            t1.join()
            t2.join()
    """
    from threading import Thread
    from functools import wraps

    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = Thread(target = func, args = args, kwargs = kwargs)
        func_hl.start()
        return func_hl

    return async_func

class Mobile():

    def __init__(self, serial_number):
        self.device = Device(serial_number)

    def print_info(self):
        logger.info('Device info: %s' % self.device.info)

    def get_object(self,**stuff):
        return self.device(**stuff)

    def get_info_of_object(self, obj):
        return obj.info

    def example_keyword(self, **stuff):
        for name, value in stuff.items():
            print name, value
        print stuff

    @run_async
    def press_power(self):
        self.device.press.power()

    @run_async
    def press_home(self):
        self.device.press.home()

    @run_async
    def click(self, **stuff):
        self.device(**stuff).click()

    def call(self, obj, method, **stuff):
        func = getattr(obj, method)
        return func(**stuff)

    def wait_until(self, *stuff):
        for something in stuff :
            something.join()

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