# -*- coding: utf-8 -*-
'''
Created on 2014/5/1

@author: YuMing
'''

import base64
import requests
import time

class ApHelper:
    def change_ssid(self, ssid, account, password):
        """
                        修改AP的SSID
                        需要先裝requests模組，指令如下
        pip install requests
        """
        account_info = ':'.join((account, password))
        authorization = base64.b64encode(account_info)
        headers = {
        'Authorization':'Basic '+authorization
        }

        form = {
        'WIFISsid0Enable':'1',
        'WIFISsid0':ssid,
        'WIFIChannel':'0',
        'WIFIHTBW':'0'
        }
        
        for times in range(1, 11):
            try:
                login_request = requests.get('http://192.168.11.1/', headers=headers)
                if login_request.status_code is requests.codes.ok: # requests.codes.ok = 200
                    change_ssid_request = requests.post('http://192.168.11.1/wizard_func_wlan_channel.html', data=form, headers=headers)
                    if change_ssid_request.status_code is requests.codes.ok:
                        print 'change ssid successfully'
                    else:
                        print 'change ssid fail'
                    break
                else:
                    print 'this is %d times to try connection login' % times
                    time.sleep(60) # 60sec
                    if times is 10:
                        print 'change ssid timeout'
            except requests.ConnectionError:
                print 'Max retries exceeded with url'
                break
# def __init__():
#     pass

def change_ssid(ssid):
    apHelper = ApHelper()
    apHelper.change_ssid(ssid, 'admin', 'ATA2013')