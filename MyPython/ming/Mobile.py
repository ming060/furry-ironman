# -*- coding: utf-8 -*-
from robot.api import logger
from uiautomator import Device, device

class Mobile():

    def __init__(self, android_serial = None):
        if android_serial is None:
            self.device = device
        else:
            self.device = Device(android_serial)

    def get_info(self):
        """
        Retrieve the device info
        """
        return self.device.info

#Key Event Actions of the device
    """
    Turn on/off screen
    """
    def turn_on_screen(self):
        """
        Turn on screen
        """
        self.device.screen.on()

    def turn_off_screen(self):
        """
        Turn off screen
        """
        self.device.screen.off()

    def wakeup_the_device(self):
        """
        wakeup the device
        """
        self.device.wakeup()

    def sleep(self):
        """
        sleep the device, same as turning off the screen.
        """
        self.device.sleep()

    """
    Press hard/soft key
    """

    def press_key(self, *key):
        """
        press *key* keycode
        """
        self.device.press(*key)

    def press_home(self):
        """
        press home key
        """
        self.device.press.home()

    def press_back(self):
        """
        press back key
        """
        self.device.press.back()

    def press_left(self):
        """
        press left key
        """
        self.device.pres.left()

    def press_right(self):
        """
        press right key
        """
        self.device.press.right()

    def press_up(self):
        """
        press up key
        """
        self.device.press.up()

    def press_down(self):
        """
        press down key
        """
        self.device.press.down()

    def press_center(self):
        """
        press center key
        """
        self.device.press.center()

    def press_menu(self):
        """
        press menu key
        """
        self.device.press.menu()

    def press_search(self):
        """
        press search key
        """
        self.device.press.search()

    def press_enter(self):
        """
        press enter key
        """
        self.device.press.enter()

    def press_delete(self):
        """
        press delete key
        """
        self.device.press.delete()

    def press_recent(self):
        """
        press recent key
        """
        self.device.press.recent()

    def press_volume_up(self):
        """
        press volume up key
        """
        self.device.press.volume_up()

    def press_volume_down(self):
        """
        press volume down key
        """
        self.device.press.volume_down()

    def press_camera(self):
        """
        press camera key
        """
        self.device.press.camera()

    def press_power(self):
        """
        press power key
        """
        self.device.press.power()

#Gesture interaction of the device

    def click(self, x, y):
        """
        click (x, y) on screen
        """
        self.device.click(x, y)

    def swipe(self, sx, sy, ex, ey, steps=10):
        """
        swipe from (sx, sy) to (ex, ey) with steps
        """
        self.device.swipe(sx, sy, ex, ey, steps)

    def drag(self,sx, sy, ex, ey, steps=10):
        """
        not test yet desire z only API 17 does not support
        drag from (sx, sy) to (ex, ey) with steps
        """
        self.device.drag(sx, sy, ex, ey, steps)

    #Wait until the specific ui object appears or gone

    # wait until the ui object appears
    def wait_for_exists(self, obj, timeout=0):
        """
        true means the object exist
        false means the object does not exist
        in the given timeout
        """
        return obj.wait.exists(timeout=timeout)

    # wait until the ui object gone
    def wait_until_gone(self, obj, timeout=0):
        """
        true means the object disappear
        false means the object exist
        in the given timeout
        """
        return obj.wait.gone(timeout=timeout)

#Screen Actions of the device
#Watcher
#     def (self):
#         """
#          
#         """
#         self.device
#Selector

    def get_object(self, **attribute):
        """
        get the ui object with attribute *attribute*
        """
        return self.device(**attribute)

    def get_info_of_object(self, obj):
        return obj.info

    def click_on(self, **attribute):
        """
        click on the object with *attribute*
        """
        self.device(**attribute).click()

    def long_click_on(self, **attribute):
        """
        click on the object with *attribute*
        """
        self.device(**attribute).long_click()

    def call(self, obj, method, **attribute):
        func = getattr(obj, method)
        return func(**attribute)

if __name__ == '__main__':
    print 'start'

    m = Mobile('HT12ERT00129')
    obj = m.get_object(textContains='26')
    print m.get_info_of_object(obj, 'contentDescription', 'checked')
    
#     'contentDescription', 'checked'
    
#     m.turn_off_screen()
#     m.turn_on_screen()
#     m.sleep()
#     m.wakeup_the_device()
    
#     linearLayout = m.get_object(className='android.widget.LinearLayout', index=2)
#     info_dict = m.get_info_of_object(linearLayout)
#     print info_dict
#     print info_dict['chileCount']
#     chileCount = int(info_dict['chileCount']) - 1
#     print chileCount
#     btn = m.call(linearLayout, 'child', instance=chileCount, className='android.widget.ImageView')
#     m.call(btn, 'click')

    print 'end'