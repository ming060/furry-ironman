'''
Created on 2014/3/31

@author: YuMing
'''
from uiautomator import device as d

if __name__ == '__main__':

    d.press.home()

    view = d(className='android.view.View', index=4)

    all_apps_button = view.child(className='android.widget.TextView', index=2)
    all_apps_button.click()

    google_play_icon = d(description='Shop')
    google_play_icon.click()

    play_store_text = d(text='Play Store')
    assert play_store_text.wait.exists(timeout=5000), 'Play Store Text does not exist.'