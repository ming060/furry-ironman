# -*- coding: utf-8 -*-
from robot.api import logger
from uiautomator import Device
import subprocess
import os
from robot.output.monitor import CommandLineWriter as clm

# logger.info("Importing Android library")
# print "Importing Android library"
# clm = CommandLineWriter()
# clm.message("Importing Android library")

class TestHelper:
    def __init__(self, serial_number=None):
        self.serial_number = serial_number

    def __convert_to_unicode_by_text(self, text):
        """
                        將輸入的字串轉換成 Unicode Transformation Format (UTF-8)
        """
        # 由object轉換為string之後，移除前後的unicode標記，例如：將u'abc'轉換為字串abc
        return repr(text)[2:-1]

    def send_set_text_cmd(self, text):
        """
        shell指令使用雙引號括起來，例如：adb shell "am broadcast -a myIME.intent.action.pass.string -e input abc"
                        但由於內容也可能為包含符號或是空白，所以必須再使用雙引號括起來，例如："abc c"
        """
        adb = ADB(self.serial_number)
        adb.shell_cmd('\"am broadcast -a myIME.intent.action.pass.string -e input \\\"%s\\\"\"' % TestHelper.__convert_to_unicode_by_text(self, text))
        adb.shell_cmd('input keyevent KEYCODE_UNKNOWN')

class ADB:
    def __init__(self, android_serial=None):
        self.buf = []
        self.buf.append('adb ')
        self.prefix_cmd = ''.join(self.buf)
        if android_serial is not None :
            self.buf.append('-s %s ' % android_serial)
            self.prefix_cmd = ''.join(self.buf)

    def cmd(self, cmd):
        """
                        將 adb -s SERIAL_NUMBER xxxxxx or adb xxxxxxx 取代成 xxxxxx
        """
        self.buf = []
        self.buf.append(self.prefix_cmd)
        self.buf.append(cmd)
        cmd = ''.join(self.buf)
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    def shell_cmd(self, cmd):
        """
                        將 adb -s SERIAL_NUMBER shell xxxxxx or adb shell xxxxxxx 取代成 xxxxx-x
        """
        self.buf = []
        self.buf.append(self.prefix_cmd)
        self.buf.append('shell ')
        self.buf.append(cmd)
        cmd = ''.join(self.buf)
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

class Mobile():
    """
    """

    def __init__(self, android_serial = None):
#         logger.info("Importing Android library")
#         print "Importing Android library"
#         clm.message("Importing Android library")
        self.adb = ADB(android_serial)
        self.device = Device(android_serial)
        self.test_helper = TestHelper(android_serial)

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

#     def sleep(self):
#         """
#         sleep the device, same as turning off the screen.
#         """
#         self.device.sleep()

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

# Swipe from the center of the ui object to its edge

    def swipe_left(self, obj, steps=10):
        """
        swipe the *obj* from center to left
        """
        obj.swipe.left(steps=steps)

    def swipe_right(self, obj, steps=10):
        """
        swipe the *obj* from center to right
        """
        obj.swipe.right(steps=steps)

    def swipe_top(self, obj, steps=10):
        """
        swipe the *obj* from center to top
        """
        obj.swipe.top(steps=steps)

    def swipe_bottom(self, obj, steps=10):
        """
        swipe the *obj* from center to bottom
        """
        obj.swipe.bottom(steps=steps)

    def drag(self,sx, sy, ex, ey, steps=10):
        """
        not test yet desire z only API 17 does not support
        drag from (sx, sy) to (ex, ey) with steps
        """
        self.device.drag(sx, sy, ex, ey, steps)

    #Wait until the specific ui object appears or gone

    # wait until the ui object appears
    def wait_for_exists(self, timeout=0, *args, **attribute):
        """
        true means the object which has *attribute* exist
        false means the object does not exist
        in the given timeout
        """
        return self.device(**attribute).wait.exists(timeout=timeout)

    # wait until the ui object gone
    def wait_until_gone(self, timeout=0, *args, **attribute):
        """
        true means the object which has *attribute* disappear
        false means the object exist
        in the given timeout
        """
        return self.device(**attribute).wait.gone(timeout=timeout)

    def wait_for_object_exists(self, obj, timeout=0):
        """
        true means the object exist
        false means the object does not exist
        in the given timeout
        """
        return obj.wait.exists(timeout=timeout)

    # wait until the ui object gone
    def wait_until_object_gone(self, obj, timeout=0):
        """
        true means the object disappear
        false means the object exist
        in the given timeout
        """
        return obj.wait.gone(timeout=timeout)


    # Perform fling on the specific ui object(scrollable)
    def fling_forward_horizontally(self, obj):
        """
        return whether the object can be fling or not
        """
        return obj.fling.horiz.forward()

    def fling_backward_horizontally(self, obj):
        """
        return whether the object can be fling or not
        """
        return obj.fling.horiz.backward()

    def fling_forward_vertically(self, obj):
        """
        return whether the object can be fling or not
        """
        return obj.fling.vert.forward()

    def fling_backward_vertically(self, obj):
        """
        return whether the object can be fling or not
        """
        return obj.fling.vert.backward()

    # Perform scroll on the specific ui object(scrollable)

    def scroll_forward_horizontally(self, obj, steps=10):
        """
        return whether the object can be fling or not
        """
        return obj.scroll.horiz.forward(steps=steps)

    def scroll_backward_horizontally(self, obj, steps=10):
        """
        return whether the object can be fling or not
        """
        return obj.scroll.horiz.backward(steps=steps)

    def scroll_to_horizontally(self, obj, *args,**attribute):
        """
        return whether the object can be fling or not
        """
        return obj.scroll.horiz.to(**attribute)

    def scroll_forward_vertically(self, obj, steps=10):
        """
        return whether the object can be fling or not
        """
        return obj.scroll.vert.forward(steps=steps)

    def scroll_backward_vertically(self, obj, steps=10):
        """
        return whether the object can be fling or not
        """
        return obj.scroll.vert.backward(steps=steps)

    def scroll_to_vertically(self, obj, *args, **attribute):
        """
        return whether the object can be fling or not
        """
        return obj.scroll.vert.to(**attribute)

#Screen Actions of the device
#Watcher
#     def register_click_watcher(self, watcher_name, attributes, *condition_list):
#         """
#         The watcher click on the object which has the attributes when conditions match
#         """
#         print type(attributes)
#         watcher = self.device.watcher(watcher_name)
#         for condition in condition_list:
#             watcher.when(**condition)
#         watcher.click(**attributes)
#         self.device.watchers.run()
#         print 'register watcher:%s' % watcher_name
#         return

    def __unicode_to_dict(self, a_unicode):
        a_dict = dict()
        dict_item_count = a_unicode.count('=')
        for count in range(dict_item_count):
            equal_sign_position = a_unicode.find('=')
            comma_position = a_unicode.find(',')
            a_key = a_unicode[0:equal_sign_position]
            if comma_position == -1:
                a_value = a_unicode[equal_sign_position + 1:]
            else:
                a_value = a_unicode[equal_sign_position + 1:comma_position]
                a_unicode = a_unicode[comma_position + 1:]
            a_dict[a_key] = a_value
        return a_dict

    def register_click_watcher(self, watcher_name, attributes, *condition_list):
        """
        The watcher click on the object which has the *attributes* when conditions match
        """
        watcher = self.device.watcher(watcher_name)
        for condition in condition_list:
            watcher.when(**self.__unicode_to_dict(condition))
        watcher.click(**self.__unicode_to_dict(attributes))
        self.device.watchers.run()

    def register_press_watcher(self, watcher_name, press_keys, *condition_list):
        """
        The watcher perform *press_keys* action sequentially when conditions match
        """
        def unicode_to_list(a_unicode):
            a_list = list()
            comma_count = a_unicode.count(',')
            for count in range(comma_count + 1):
                comma_position = a_unicode.find(',')
                if comma_position == -1:
                    a_list.append(str(a_unicode))
                else:
                    a_list.append(a_unicode[0:comma_position])
                    a_unicode = a_unicode[comma_position + 1:]
            return a_list

        watcher = self.device.watcher(watcher_name)
        for condition in condition_list:
            watcher.when(**self.__unicode_to_dict(condition))
        watcher.press(*unicode_to_list(press_keys))
        self.device.watchers.run()

    def remove_watchers(self, watcher_name = None):
        """
        remove watcher with *watcher_name* or remove all watchers
        """
        if watcher_name == None:
            self.device.watchers.remove()
        else:
            self.device.watchers.remove(watcher_name)

    def list_all_watchers(self):
        """
        return the watcher list
        """
        return self.device.watchers
#Selector

    def get_object(self, *args, **attribute):
        """
        get the ui object with attribute *attribute*
        """
        return self.device(*args, **attribute)

    def get_info_of_object(self, obj):
        """
        return info dictionary of the *obj*
        The info example:
        {
         u'contentDescription': u'',
         u'checked': False,
         u'scrollable': True,
         u'text': u'',
         u'packageName': u'com.android.launcher',
         u'selected': False,
         u'enabled': True,
         u'bounds': 
                   {
                    u'top': 231,
                    u'left': 0,
                    u'right': 1080,
                    u'bottom': 1776
                   },
         u'className': u'android.view.View',
         u'focusable': False,
         u'focused': False,
         u'clickable': False,
         u'checkable': False,
         u'chileCount': 1,
         u'longClickable': False,
         u'visibleBounds':
                          {
                           u'top': 231,
                           u'left': 0,
                           u'right': 1080,
                           u'bottom': 1776
                          }
        }
        """
        return obj.info

    def click_on(self, *args, **attribute):
        """
        click on the object with *attribute*
        """
        self.device(**attribute).click()

    def long_click_on(self, *args, **attribute):
        """
        click on the object with *attribute*
        """
        self.device(**attribute).long_click()

    def call(self, obj, method, *args, **attribute):
        func = getattr(obj, method)
        return func(**attribute)

    def set_text(self, text, *args, **attribute):
        """
        set *text* to the Component which has the *attribute* 
        """
        self.device(**attribute).set_text(text)

# Other feature

    def sleep(self, time):
        """
        sleep(no action) for *time* (in millisecond)
        """
        target = 'wait for %s' % str(time)
        self.device(text=target).wait.exists(timeout=time)

    def install(self, apk_path):
        self.adb.cmd('install "%s"' % apk_path)

    def uninstall(self, package_name):
        self.adb.cmd('uninstall %s' % package_name)

    def type(self, text):
        """
        Type *text* at current focused component
        """
        self.test_helper.send_set_text_cmd(text)

    def foo(self):
        pass
#         clm = CommandLineWriter()
        # output some messages on console
#         clm.message(' ')
#         clm.message(u'中文')
#         clm.message(u'2----------2')

if __name__ == '__main__':
    print 'start'

    m = Mobile()

#     dict = {'text':'音樂'}
#     m.register_click_watcher('music', text='音樂', dict)
    
#     m = Mobile('192.168.185.101:5555')
#     m.uninstall('com.dropbox.android')
#     m.install('C:\\Users\\YuMing\\Documents\\GitHub\\furry-ironman\\RF_uiautomator\\com.dropbox.android_2.4.0.2.apk')
#     m.wakeup_the_device()
#   
#     info = m.get_info()
#     if info['currentPackageName'] == 'com.android.keyguard':
#         m.swipe(540, 1335, 900, 1335, 5)
#   
#     m.press_home()
#     m.click_on(description='Apps')
#     m.click_on(text='Dropbox')
#  
#     m.click_on(text='Sign in!')
#  
#     m.set_text('lym060@gmail.com', resourceId='com.dropbox.android:id/login_email')
#     m.set_text('ginobili060', resourceId='com.dropbox.android:id/login_password')
#     m.click_on(resourceId='com.dropbox.android:id/login_submit')

#     print m.get_info()
# #     {u'displayRotation': 0, u'displaySizeDpY': 640, u'displaySizeDpX': 360, u'currentPackageName': u'com.android.launcher', u'productName': u'vbox86p', u'displayWidth': 1080, u'sdkInt': 19, u'displayHeight': 1776, u'naturalOrientation': True}
#     m.click_on(description='Apps')
#     view = m.get_object(resourceId='com.android.launcher:id/apps_customize_pane_content')
#     print m.get_info_of_object(view)
# #     {u'contentDescription': u'', u'checked': False, u'scrollable': True, u'text': u'', u'packageName': u'com.android.launcher', u'selected': False, u'enabled': True, u'bounds': {u'top': 231, u'left': 0, u'right': 1080, u'bottom': 1776}, u'className': u'android.view.View', u'focusable': False, u'focused': False, u'clickable': False, u'checkable': False, u'chileCount': 1, u'longClickable': False, u'visibleBounds': {u'top': 231, u'left': 0, u'right': 1080, u'bottom': 1776}}

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